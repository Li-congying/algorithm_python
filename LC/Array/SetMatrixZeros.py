'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        [[0]]
        """
        cols = {}
        rows = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    cols[j] = 1
                    rows[i] = 1

        for c in cols:
            for i in range(len(matrix)):
                matrix[i][c] = 0
        for r in rows:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0

        print matrix


obj = Solution()
obj.setZeroes( [[0, 1],
                [1, 0]])
