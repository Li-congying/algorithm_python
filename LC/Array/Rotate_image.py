'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])-i):
                #print (i, j),
                matrix[i][j], matrix[n-j][n-i] =  matrix[n-j][n-i], matrix[i][j]
        for i in range(len(matrix)/2):
            matrix[i], matrix[0-i-1] = matrix[0-i-1], matrix[i]

        return matrix

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
obj = Solution()
obj.rotate(matrix)