def alienOrder(words):
    """
    :type words: List[str]
    :rtype: str
    """
    if len(words) == 1:
        return words[0][::-1]

    list_ = []
    indegree = {}
    edge = {}
    empty_set = []


    for word in words:
        for i in range(len(word)):
            if word[i] not in indegree:
                indegree[word[i]] = 0
                edge[word[i]] = {}
            # if i >= 1 and word[i] != word[i-1] and word[i] not in edge[word[i-1]]:
            #     edge[word[i-1]][word[i]] = 1
            #     indegree[word[i]] += 1

    for i in range(1, len(words)):
        j = 0
        while j < len(words[i-1]) and j < len(words[i]):
            if (j == 0 or words[i-1][j-1] == words[i][j-1]) and words[i-1][j] != words[i][j] and words[i][j] not in edge[words[i-1][j]]:
                edge[words[i-1][j]][words[i][j]] = 1
                indegree[words[i][j]] += 1
            j+=1

    for i in indegree:
        if indegree[i] == 0:
            empty_set.append(i)

    print indegree, edge, empty_set

    while len(empty_set):
        key = empty_set.pop()
        del(indegree[key])
        for node in edge[key]:
            indegree[node] -= 1
            if indegree[node] <= 0:
                empty_set.append(node)
        list_.append(key)
        #if len(list_) == 0 and len(indegree):


        print list_
        print indegree, edge

    print list_, indegree

    return  "".join(list_) if indegree == {} else ""


# print alienOrder([
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ])

input = ["wrt",
         "wrf",
         "er",
         "ett",
         "rftt"
         ]


words = ["ab", 'ac', 'dc', 'db']


def alienDict(words):
    indegree = {w: 0 for word in words for w in word}
    g = {}

    for i in range(len(words) - 1):
        j = 0
        while j < len(words[i]) and j < len(words[i + 1]):
            if words[i][j] != words[i + 1][j]:
                if words[i][j] not in g:
                    g[words[i][j]] = []
                if words[i + 1][j] not in g[words[i][j]]:
                    g[words[i][j]].append(words[i + 1][j])
                    indegree[words[i + 1][j]] += 1
                break
            j += 1

    empty_list = []
    for node in indegree:
        if indegree[node] == 0:
            empty_list.append(node)

    result = []
    while empty_list:
        node = empty_list.pop()
        del (indegree[node])
        result.append(node)
        if node in g:
            for nxt in g[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    empty_list.append(nxt)

    return "".join(result) if not indegree else ""


print alienDict(words)

# a = ['aa','bb',5]
# b = ['cc','dd']
# print zip(a, b)

a = ['1c', '2']
b = ['2d', '3']

print zip(a, b)
# print a - b