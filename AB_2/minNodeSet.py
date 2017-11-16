g = {0: [2, 3], 1: [0], 2: [1], 3: [], 4: [3]}


def getMinNodeSet(g):
    def helper(g, node, visited, path):
        if node in visited:
            return
        visited.add(node)
        for nxt in g[node]:
            helper(g, nxt, visited, path)

        path.append(node)

    path = []
    visited = set()
    for node in g:
        helper(g, node, visited, path)

    # print path
    visited = set()
    result = []
    for node in path[::-1]:
        if node not in visited:
            result.append(node)
            helper(g, node, visited, path)

    print result


getMinNodeSet(g)