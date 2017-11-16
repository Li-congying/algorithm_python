board = [['a', 'b', 'c'], ['b', 'c', 'a'], ['d', 'e', 'f']]
words = ['abc', 'cbc', 'bc', 'ce', 'afe', 'ab']

def wordSearch(board, root):
    result = {}
    def search(board, i, j, node, set_ = [], str_ = ""):
        if i < 0 or j< 0 or i >= len(board) or j >= len(board[i]):
            return
        if (i, j) in set_:
            return
        if board[i][j] not in node:
            return
        set_.append((i,j))
        str_ += board[i][j]
        node = node[board[i][j]]
        if '#' in node:
            if str_ not in result:
                result[str_] = []
            result[str_].append(set_)

        search(board, i - 1, j, node, set_[:], str_)
        search(board, i + 1, j, node, set_[:], str_)
        search(board, i , j-1, node, set_[:], str_)
        search(board, i , j+1, node, set_[:], str_)

    for i in range(len(board)):
        for j in range(len(board[i])):
            search(board, i, j, root, [])

    return result

def boggleGame(board, words):
    # build trie
    root = {}
    for word in words:
        node = root
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]] = {}
            node = node[word[i]]
            if i == len(word) -1:
                node['#'] = 1


    match_list = wordSearch(board, root)

    def dfs(match_list, index, all_points, result):
        if index >= len(match_list):
            return
        key = match_list.keys()[index]
        find = False
        for lt in match_list[key]:
            status = True
            for (i,j) in lt:
                if (i,j) in all_points:
                    status = False
                    break
            if status:
                result.add(key)
                find = True
                dfs(match_list, index+1, all_points+lt, result)
        if not find:
            dfs(match_list, index+1, all_points, result)

    for i in range(len(match_list.keys())):
        result = set()
        dfs(match_list, i, [], result)
        print i, match_list.keys()[i], result



boggleGame(board, words)

