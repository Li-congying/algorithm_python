'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.result = []

        def getBoundry(matrix, result):

            if not matrix or not matrix[0]:
                return []
            if matrix[0]:
                result += matrix.pop(0)
                if len(matrix):
                    j = 0
                    while j < len(matrix) and len(matrix):
                        result.append(matrix[j].pop())
                        if len(matrix[j]) == 0:
                            del (matrix[j])
                        else:
                            j += 1
                    if len(matrix):
                        result += matrix.pop(-1)[::-1]
                        j = len(matrix) - 1
                        print matrix
                        while j >= 0  and len(matrix):
                            result.append(matrix[j].pop(0))
                            if len(matrix[j]) == 0:
                                del (matrix[j])
                                j -= 1

            if matrix:
                getBoundry(matrix, self.result)

        getBoundry(matrix, self.result)
        return self.result

matrix = [[1,11,4],[2,12,6],[3,13,5]]

obj = Solution()
print obj.spiralOrder(matrix)



