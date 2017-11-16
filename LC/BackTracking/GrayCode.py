'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, 
print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        hash_map = {}
        for n_i in range(n+1):
            base = n_i
            hash_map[n_i] = {}
            count = 0
            while base:
                if base & 01 == 1:
                    hash_map[n_i][n_i - 2**count] = 1
                    hash_map[n_i - 2**count][n_i] = 1
                # else:
                #     hash_map[n_i][n_i + 2**count] = 1
                base = base >> 1
                count += 1
        self.result = []
        def helper(cur, visited, result, n, graph):

            result.append(cur)
            if len(result) == n:
                self.result = result
                return True
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited[nxt] = 1
                    ret = helper(nxt, visited, result, n, graph)
                    if ret:
                        return True
                    del(visited[nxt])

            return False

        for i in range(n):
            visited = {i:1}
            helper(i, visited, [], n, hash_map)

        for i in self.result:
            print bin(i)," "

obj = Solution()
obj.grayCode(8)