def preferenceList(plist):
    # graph
    elements = set([c for p in plist for c in p])
    g = {w: list() for w in elements}
    for p in plist:
        for i in range(1, len(p)):
            g[p[i - 1]].append(p[i])

    def dfs(e, visited, recStk):
        if e in visited:
            return

        visited.add(e)
        for nei in g[e]:
            dfs(nei, visited, recStk)

        recStk.append(e)

    stk = []
    visited = set()
    for e in elements:
        dfs(e, visited, stk)

    return stk[::-1]


assert preferenceList([[3, 5, 7, 9], [2, 3, 8], [5, 8]]) == [2, 3, 5, 8, 7, 9]


def getPreferenceList(list = []):

    graph = {key:[] for l in list for key in l }
    for lt in list:
        for i in range(1, len(lt)):
            graph[lt[i-1]].append(lt[i])

    result = []
    def dfs(graph, key, visited):
        if key in visited:
            return
        visited[key] = 1
        for next_ in graph[key]:
            dfs(graph, next_, visited)

        result.append(key)

    visite = {}
    for lt in list:
        for n in lt:
            dfs(graph, n, visite)
    return result[::-1]


#print getPreferenceList([[3, 5, 7, 9], [2, 3, 8], [5, 8]])

input_list = [[3, 5, 7, 9], [2, 3, 8], [5, 8]]


def getPreference_list(input_list):
    pre_relation = {}

    for list_ in input_list:
        for i in range(1, len(list_)):
            if i >= 1:
                if list_[i - 1] not in pre_relation:
                    pre_relation[list_[i - 1]] = []
                pre_relation[list_[i - 1]].append(list_[i])

    pre_list = []

    # used = {}
    def dfs(pre_relation, i, used):
        if i in used:
            return
        used[i] = 1
        # print i, pre_relation
        # if i in pre_relation:
        for nxt in pre_relation[i]:
            dfs(pre_relation, nxt, used)
        pre_list.append(i)

    visite = {}
    for list_ in input_list:
        for key in list_:
            # print visite
            dfs(pre_relation, key, visite)

    print pre_list[::-1]
    return pre_list[::-1]

getPreferenceList(input_list)
getPreference_list(input_list)

