def searchWord(board=[], word=""):
    if len(word) == 0:
        return True

    #cur_set = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            cur_set = {}
            if dfs(board, word, i, j, cur_set):
                return True
    else:
        return False


def dfs(board, s, i, j, set_):

    if len(s) == 0:
        return True
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
        return False
    print i, j, s, set_
    if s[0] != board[i][j]:
        return False
    key = str(i)+"_"+str(j)
    if key in set_:
        return False
    set_[key] = 1

    return  dfs(board, s[1:], i-1, j, set_.copy()) or  dfs(board, s[1:], i+1, j, set_.copy()) or dfs(board, s[1:], i, j - 1, set_.copy()) or dfs(board, s[1:], i, j+1, set_.copy())




class TrieNode(object):
    def __init__(self, x, status = False):
        self.val = x
        self.chil = {}
        self.status = status

class Trie(object):
    def __init__(self, x="", status=False):
        self.root = TrieNode(x, status)

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            next_node = None
            if word[i] in node.chil:
                next_node = node.chil[word[i]]
            if not next_node:
                next_node = TrieNode(word[i])
                node.chil[word[i]] = next_node
            if i == len(word)-1:

                next_node.status = True
            node = next_node

    # def search(self, word):
    #     node = self.root
    #     for i in range(len(word)):
    #         #next_node = None
    #         if word[i] not in node.chil:
    #             return False
    #         next_node = node.chil[word[i]]
    #         node = next_node
    #     return node.status
    #     #return node
    #
    # def startWith(self, prefix):
    #     if len(prefix) == 0:
    #         return True
    #     node = self.root
    #     for i in range(len(prefix)):
    #         # next_node = None
    #         if prefix[i] not in node.chil:
    #             return False
    #         next_node = node.chil[prefix[i]]
    #         node = next_node
    #     else:
    #         return Trie(node.val, node.status)




def searchWord2(board, word_list):
    nodes = {}
    for word in word_list:
        node = nodes
        for s in range(len(word)):
            if word[s] not in node:
                node[word[s]] = {}
            node = node[word[s]]
            if s == len(word) -1:
                node['#'] = 1

    match_list = []
    def dfs(board, prefix, i, j, set_, node):
        if i < 0 or j<0 or i >=len(board) or j >= len(board[i]):
            return False
        #print 'start', prefix, i, j, board[i][j], set_
        key = str(i) + "_" + str(j)
        if key in set_:
            return False
        #prefix = prefix+str(board[i][j])
        #new_tri = tri.startWith(board[i][j])
        if board[i][j] not in node:
            return False
        next_node = node[board[i][j]]


        prefix = prefix + str(board[i][j])
        if '#' in next_node:
            if prefix not in match_list:
                match_list.append(prefix)

        set_[key] = 1

        dfs(board, prefix, i+1, j, set_.copy(), next_node)
        dfs(board, prefix, i-1, j, set_.copy(), next_node)
        dfs(board, prefix, i, j + 1, set_.copy(), next_node)
        dfs(board, prefix, i, j - 1, set_.copy(), next_node)

    for i in range(len(board)):
        for j in range(len(board[i])):
            set_ = {}
            prefix = ""
            dfs(board, prefix, i, j, set_, nodes)

    return match_list





board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
#board = ["a"]


#print searchWord2(board, ['oath', 'oe','flv', 'erv', 'taea'])
print searchWord2("a", "aa")