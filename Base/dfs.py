class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        candy = set(range(len(M)))
        c = 0
        while candy:
            stack = [candy.pop()]
            c += 1
            while stack:
                p = stack.pop()
                for i in range(len(M)):
                    if M[p][i] == 1 and i in candy:
                        candy.discard(i)
                        stack.append(i)
        return c

