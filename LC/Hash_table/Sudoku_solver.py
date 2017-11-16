'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def checkRemain(board, row, col):
            remain = set([str(i) for i in range(1, 10)])
            for i in range(len(board)):
                #print row,i, board[row][i], i, col, board[i][col], remain
                if board[row][i] != '.' and board[row][i] in remain:
                    #del(remain[board[row][i]])
                    remain.remove(board[row][i])
                if board[i][col] != '.' and board[i][col] in remain:
                    remain.remove(board[i][col])

            x = (row/3) * 3
            y = (col/3) * 3
            for k in range(9):
                #print x, y
                #print row, col, x, y, x+k/3, y+k%3
                if board[x+k/3][y+k%3] != '.' and board[x+k/3][y+k%3] in remain:
                    remain.remove(board[x+k/3][y+k%3])
            return remain

        def helper(board, row, col):
            #print row, col

            if col == len(board[row]):
                col = 0
                row += 1
            if row >= len(board):
                return True
            if board[row][col] == '.':
                remain = checkRemain(board, row, col)
                #print remain
                if not remain:
                    return False
                for val in remain:
                    board[row][col] = val
                    if helper(board, row, col+1):
                        return True
                    board[row][col] = '.'
            else:
                return helper(board, row, col+1)

        helper(board, 0, 0)
        print board







board = [["5",".","9","7","4","8",".",".","."],
         ["7","8",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]

# board =[
# ['1', '3', '9', '7', '4', '8', '6', '5', '2'],
# ['7', '4', '5', '3', '2', '6', '1', '8', '9'],
# ['8', '2', '6', '1', '5', '9', '4', '3', '7'],
# ['3', '1', '7', '5', '.', '.', '2', '4', '.'],
# ['.', '6', '4', '.', '1', '.', '5', '9', '.'],
# ['.', '9', '8', '.', '.', '.', '3', '.', '.'],
# ['.', '.', '.', '8', '.', '3', '.', '2', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '6'],
# ['.', '.', '.', '2', '7', '5', '9', '.', '.']]

board_solve = [["5","1","9","7","4","8","6","3","2"],
         ["7","8","3","6","5","2","4","1","9"],
         ["4","2","6","1","3","9","8","7","5"],
         ["3","5","7","9","8","6","2","4","1"],
         ["2","6","4","3","1","7","5","9","8"],
         ["1","9","8","5","2","4","3","6","7"],
         ["9","7","5","8","6","3","1","2","4"],
         ["8","3","2","4","9","1","7","5","6"],
         ["6","4","1","2","7","5","9","8","3"]]

obj = Solution()
obj.solveSudoku(board)

# for row in range(9):
#     for col in range(9):
#         print 'r',row, 'c', col
#         x = (row / 3) * 3
#         y = (col / 3) * 3
#         print 'x',x, 'y',y
#         for k in range(9):
#             print  (x+k/3, y+k%3),
#         print '\n'
#             # # print row, col, x, y, x+k/3, y+k%3
            # if board[x + k / 3][y + k % 3] != '.' and board[x + k / 3][y + k % 3] in remain:
            #     remain.remove(board[x + k / 3][y + k % 3])
