'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, 
and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , 
where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''

'''
[ ["a","b"],["b","c"] ]
[2.0,3.0]
[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]

[6.00000,3.00000,-1.00000,1.00000,-1.00000]
'''

import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for i in range(len(equations)):
            if equations[i][0] not in graph:
                graph[equations[i][0]] = {}
            graph[equations[i][0]][equations[i][1]] = values[i]
            if equations[i][1] not in graph:
                graph[equations[i][1]] = {}
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]


        def helper(dividend, divisor, graph, cur, visited):
            #print dividend, divisor, cur
            if dividend not in graph or dividend in visited:
                return False
            if dividend == divisor:
                return 1.0
            visited[dividend] = 1
            if divisor in graph[dividend]:
                return cur * graph[dividend][divisor]
            for nxt in graph[dividend]:
                ret = helper(nxt, divisor, graph, cur*graph[dividend][nxt], visited)
                if ret:
                    return ret
        result = []
        for dividend , divisor in queries:
            ret = helper(dividend, divisor, graph, 1, {})
            if not ret:
               result.append(-1.0)
            else:
                result.append(ret)

        return result

    def solution(self, equations, values, queries):
        quot = collections.defaultdict(dict)
        print (quot)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        for k in quot:
            for i in quot[k]:
                for j in quot[k]:
                    quot[i][j] = quot[i][k] * quot[k][j]
        return [quot[num].get(den, -1.0) for num, den in queries]


obj = Solution()

aa = obj.solution([["a","e"],["b","e"],["a", "c"], ["a", "b"]],[4.0,3.0, 1.0, 10.0],[["a","b"],["b","c"],["x","x"]])
print (aa)
