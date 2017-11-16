import sys
def shortestpath(g, start, end, k):
    if start == end: return 0
    min_cost = sys.maxint
    q = [(start, 0)]
    step = 0
    if step == k:
        return min_cost

    while q:
        next = []
        for cur, cost in q:
            for nei, c in g.get(cur, []):
                if nei == end:
                    min_cost = min(min_cost, cost + c)
                else:
                    next.append((nei, cost + c))

        step += 1
        if step == k:
            return min_cost
        q = next

    return min_cost


g = {'A': [('B', 100), ('C', 500)], 'B': [('C', 100)]}
#print shortestpath(g, 'A', 'C', 2)

def getMinCost(g, departure, arrive, k):

    min_cost = float('+inf')

    queue = [[departure, 1, 0]]
    visited = {}
    while len(queue):
        node = queue[0]
        visited[node[0]] = 1
        del (queue[0])
        if node[1] > k:
            break
        print node[0]
        for next_ in g[node[0]]:
            print node[0], next_, node[2]
            if next_[0] == arrive:
                min_cost = min(min_cost, node[2] + next_[1])
                visited[next_[0]] = 1
            if next_[0] in g and next_ not in visited and node[2]+ next_[1] <= min_cost:
                queue.append([next_[0], node[1]+1, node[2]+ next_[1]])

    return min_cost


print getMinCost(g, 'A', 'C', 2)