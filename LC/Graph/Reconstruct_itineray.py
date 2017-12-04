'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, 
the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical 
order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
'''
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = { _from : [] for _from, to in tickets }
        for _from, to in tickets:
            graph[_from].append(to)

        for to_list in graph:
            graph[to_list].sort()

        length = len(tickets) + 1
        self.result = []

        def helper(graph, node, path):

            if len(path) == length:
                self.result.append(path)
                return True
            if node in graph:
                index = 0
                while index < len(graph[node]):
                    nxt = graph[node][index]
                    del(graph[node][index])
                    ret = helper(graph, nxt, path + [nxt])
                    if ret:
                        break
                    graph[node].insert(index, nxt)
                    index += 1

        helper(graph, 'JFK', ['JFK'])

        return self.result


    def findItinerary2(self, tickets):
        targets = collections.defaultdict(list)

        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        print targets

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]


obj = Solution()
print obj.findItinerary2([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])