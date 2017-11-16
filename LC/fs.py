def path_split(path):
    return [frag for frag in path.split('/') if frag.strip() != '']


class FileSystem(object):
    def __init__(self):
        self.fs = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr = self.fs
        frags = path_split(path)
        for frag in frags:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]
            print curr, frag, frags
            if type(curr) == str:
                return [frags[-1]]
        return sorted(curr.keys())

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        curr = self.fs
        frags = path_split(path)
        for frag in frags:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        curr = self.fs
        frags = path_split(filePath)
        for frag in frags[:-1]:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]
        file_name = frags[-1]
        if file_name not in curr:
            curr[file_name] = ''
        curr[file_name] += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        curr = self.fs
        frags = path_split(filePath)
        for frag in frags[:-1]:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]
        file_name = frags[-1]
        return curr[file_name]


fs = FileSystem()
fs.mkdir('/a/b/c')
fs.addContentToFile('/a/b/d', 'aaa')
a = 'sss'
#print type(a) == unicode
print fs.ls('/a/b/e')

