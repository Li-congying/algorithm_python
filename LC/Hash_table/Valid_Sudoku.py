'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

each column each row each sub-9

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(len(board)):
            check_rows = {}
            for j in range(len(board[i])):
               if board[i][j] != '.' and board[i][j] in check_rows:
                   print 'row', check_rows
                   return False
               else:
                   check_rows[board[i][j]] = 1
        for j in range(len(board[0])):
            check_col = {}
            for i in range(len(board)):
                if board[i][j] != '.' and board[i][j] in check_col:
                    print 'col', check_col
                    return False
                else:
                    check_col[board[i][j]] = 1
        for i in [0, 3, 6]:
            for j in [0,3,6]:
                check_table = {}
                for k in range(9):
                    if i == 6 and j == 6:
                        print check_table,  i + k/3, j + k%3, board[i + k/3][j + k%3]
                    #print i + k/3, j + k%3
                    if board[i + k/3][j + k%3] != '.' and board[i + k/3][j+ k%3] in check_table:
                        print 'board', check_table, i, j, i + k/3, j + k%3, board[i + k/3][j + k%3]
                        return False
                    else:
                        check_table[ board[i + k/3][j + k%3] ] = 1

        return True

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in xrange(0, 9)]
        col = [set() for i in xrange(0, 9)]
        grid = [set() for i in xrange(0, 9)]

        for i in xrange(0, 9):
            for j in xrange(0, 9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                if board[i][j] in col[j]:
                    return False
                g = i / 3 * 3 + j / 3
                if board[i][j] in grid[g]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                grid[g].add(board[i][j])
        return True
obj = Solution()
board = [["4",".",".",".",".",".",".",".","."],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","2",".","3","9",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".","4",".","."],
         [".",".",".",".","9",".",".",".","."],
         [".",".",".",".","7",".",".",".","3"],
         [".",".",".",".",".",".",".",".","."],
         ["3",".",".",".",".",".","1",".","."]]
print obj.isValidSudoku(board)