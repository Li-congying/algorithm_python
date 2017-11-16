class PathNotExistedException(Exception):
    pass


class PathExistedException(Exception):
    pass


def echocallback(path, value):
    print "path: {}, value: {}".format(path, value)


class Node:
    def __init__(self, val):
        self.val = val
        self.cblist = []

    def addCallback(self, cb):
        self.cblist.append(cb)


class Filesystem:
    def __init__(self):
        self.node_map = {"": None}

    def create(self, path, value):
        idx = path.rfind('/')
        if idx == -1:
            parent = ""
        else:
            parent = path[:idx]

        if parent not in self.node_map:
            raise PathNotExistedException('parent: {} does not exist!'.format(parent))

        if path in self.node_map:
            raise PathExistedException('path: {} existed!'.format(path))

        #print path, parent
        self.node_map[path] = Node(value)
        #print self.node_map

    def setValue(self, path, value):
        try:
            node = self.node_map[path]
        except KeyError:
            raise PathNotExistedException('path: {} does not exist!'.format(path))

        pre = ""
        while path != "":
            node = self.node_map[path]
            print 'pre' , pre, node.cblist
            for cb in node.cblist:
                cb(pre, value)  # notify parent wiht pre for new value
                # there is no cb at leaves

            pre = path
            idx = path.rfind('/')
            print 'idx', idx, 'path', path, path[:2]
            if idx == -1:
                path = ""
            else:
                path = path[:idx]
            node = self.node_map[path]

    def getValue(self, path):
        try:
            node = self.node_map[path]
        except KeyError:
            raise PathNotExistedException('path does not exist!')

        return node.val

    def watch(self, path, cb):
        try:
            node = self.node_map[path]
        except KeyError:
            raise PathNotExistedException('path: {} does not exist!'.format(path))

        node.addCallback(cb)


def test0():
    fs = Filesystem()
    fs.create("/a", "foo")
    fs.watch("/a", echocallback)
    fs.create("/a/b", "bar")
    fs.watch("/a/b", echocallback)
    fs.create("/a/b/c", "foobar")
    fs.setValue("/a/b/c", "foo")
    print fs.node_map
    print '-------test0 done---------'


def test1():
    fs = Filesystem();

    fs.create("/a", "foo");
    fs.create("/a/y", "beijing");
    fs.create("/a/j", "tianjin");
    fs.create("/a/y/g", "shanghai");
    fs.create("/foo", "bar");

    try:
        fs.create("/foo", "bar");
    except Exception, e:
        print str(e)

    try:
        fs.create("/a/b/c", "bar");
    except Exception, e:
        print str(e)

    fs.setValue("/a", "bar");
    print '-------test1 done---------'


#test0()
#test1()

path = '/aaa/bbb'
idx = path.rfind('/')
print path[:idx]


