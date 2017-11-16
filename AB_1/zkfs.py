class Node(object):
    def __init__(self, val):
        self.val = val
        self.cb_list = set()
        self.children = {}


class FileSystem(object):
    def __init__(self):
        self.root = Node('')

    def splite_path(self, path):
        path_list = [i for i in path.split('/') if i != '']
        return path_list

    def create(self, path, value):

        node = self.root
        path_list = self.splite_path(path)
        print path_list
        for p in path_list:
            if p not in node.children:
                node.children[p] = Node("")
            node = node.children[p]

        node.val = value

    def set_value(self, path, value):
        node = self.root
        path_list = self.splite_path(path)
        for p in path_list:
            if p not in node.children:
               return False
            node = node.children[p]

        node.val = value
        path_list = self.splite_path(path)
        base_p = []
        node = self.root
        for p in path_list:
            node = node.children[p]
            base_p.append(p)
            print base_p, "/".join(base_p)
            for cb in node.cb_list:
                func = getattr(self, cb)
                func("/"+"/".join(base_p), node.val)

    def get_value(self, path):
        node = self.root
        path_list = self.splite_path(path)
        for p in path_list:
            if p not in node.children:
                return False
            node = node.children[p]
        value = node.val
        return value



    def watch(self, path):
        node = self.root
        path_list = self.splite_path(path)
        for p in path_list:
            if p not in node.children:
                return False
            node = node.children[p]
        node.cb_list.add('callback')

    def callback(self, path, value):
        print 'path:' + path + ' value:' + value

fs = FileSystem()
fs.create('/a/b', 'aaab')
print fs.get_value('/a/b')
fs.set_value('/a/b', 'bbbb')
print fs.get_value('/a/b')
fs.watch('/a/b')
fs.set_value('/a/b', 'cccc')