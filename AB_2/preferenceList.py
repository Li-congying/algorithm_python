input_list = [[3, 5, 7, 9], [2, 3, 8], [5, 8], [3, 10]]

def pref_list(input_list):
    g = {}
    all_node = {key: 1 for lt in input_list for key in lt}

    for lt in input_list:
        for i in range(len(lt) - 1):
            if lt[i] not in g:
                g[lt[i]] = {}
            g[lt[i]][lt[i + 1]] = 1

    print g

    def helper(g, node, visited, path):
        if node in visited:
            return
        visited.add(node)
        if node in g:
            for nxt in g[node]:
                helper(g, nxt, visited, path)
        path.append(node)

    path = []
    visited = set()
    for node in all_node:
        helper(g, node, visited, path)

    print path[::-1]


pref_list(input_list)

