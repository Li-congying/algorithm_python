from heapq import *

def wizarddist(g, target):
  q = [(0,0)] # cost, node id
  seen = set()
  while q:
    cost, v = heappop(q)
    seen.add(v)
    if v==target:
      return cost

    for nei in g.get(v, ()):
      if nei not in seen:
        c = (v-nei)*(v-nei)
        heappush(q, (cost+c, nei))

  return float("inf")

# g = {0: [1,2], 1: [0,2]}
# assert wizarddist(g, 2)==2 # the min is 2 instead of 4
# assert wizarddist(g, 3)==float("inf")
g = {0:[4], 4:[6], 5:[6], 6:[8, 9]}

def wizardMinCost(g, target):
    min_cost = float("inf")

    queue = [(0, 0)]
    visited = {}

    while len(queue):
        q = queue[0]
        del(queue[0])
        visited[q[0]] = 1
        if q[0] in g:
            for nxt in g[q[0]]:
                cost = q[1] + (nxt-q[0])**2
                if nxt == target:
                    min_cost = min(min_cost, cost)
                if nxt not in visited and nxt in g[q[0]] and cost < min_cost:
                    queue.append([nxt, cost])

    return min_cost

print wizardMinCost(g, 9)
