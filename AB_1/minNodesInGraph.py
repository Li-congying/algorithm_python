def startpoints(g):
    def helper(g, v, visited, stk):
        if visited[v]:
            return

        visited[v] = True
        for nei in g[v]:
            helper(g, nei, visited, stk)

        stk.append(v)

    stk = []
    n = len(g)
    visited = [False] * n
    for v in g:
        helper(g, v, visited, stk)

    visited = [False] * n
    res = []

    for v in stk[::-1]:
        if not visited[v]:
            res.append(v)
            helper(g, v, visited, [])

    return res


g = {0: [1], 1: [0], 2: [1]}
assert startpoints(g) == [2]
# g = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}
# assert startpoints(g) == [0]
# g = {0: [2, 3], 1: [0], 2: [1], 3: [], 4: [3]}
# assert startpoints(g) == [4, 0]

class Solution(object):

    def getMinList(self, g = {}):
        self.time = 0
        self.visited = {}
        def dfs(g, key, visited):
            self.time += 1
            if key in visited:
                return
            visited[key] = []
            visited[key].append(self.time)
            for next_key in g[key]:
                dfs(g, next_key, visited)

            self.time += 1
            visited[key].append(self.time)

        for key in g:
            dfs(g, key, self.visited)


        self.visited = sorted(self.visited.items(), key= lambda x: x[1][1], reverse=True)
        result = []
        visited = {}
        for node, time_ in self.visited:
            if node not in visited:
                dfs(g, node, visited)
                print visited
                result.append(node)
        return result




s = Solution()
print s.getMinList(g)





