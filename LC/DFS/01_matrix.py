'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        def getMinDis(x, y, value, dis_matrix, visited):
            if x < 0 or y <0 or x > len(matrix)-1 or y>len(matrix[x])-1:
                return False
            if (x,y) in visited:
                return False
            visited.add((x,y))
            # print (x,y), dis_matrix
            if dis_matrix[x][y] == -1 or value < dis_matrix[x][y]:
                # dis_matrix[x][y] = value
                dis_matrix[x][y] = value
                print (x, y), dis_matrix
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dif_x, dif_y in directions:
                    getMinDis(x + dif_x, y + dif_y, value+1, dis_matrix, visited)
            visited.remove((x,y))


        dis_matrix = [[-1 for _ in range(len(matrix[i]))] for i in range(len(matrix))]

        visited = set()

        directions = [(1,0), (-1, 0), (0, 1), (0,-1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    dis_matrix[i][j] = 0
                    for dif_x, dif_y in directions:
                        getMinDis(i+dif_x, j+dif_y, 1, dis_matrix, visited)


        return dis_matrix

    '''
    
        '''

obj = Solution()
print obj.updateMatrix([[1,1,1],[1,0,1],[1,1,1]])