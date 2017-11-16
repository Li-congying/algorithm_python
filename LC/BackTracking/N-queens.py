class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['0' for i in range(n)] for j in range(n)]
        self.result = []
        def helper(board, row_id, result, col_set):
            #print col_set
            for i in range(n):
                if i in col_set:
                    continue
                diag = False
                l = i - 1
                r = i + 1
                for k in range(row_id-1, -1, -1):
                    #print row_id, i, k, l, r
                    if l >= 0:
                        if board[k][l] == 'Q':
                            diag = True
                            break
                        l -= 1
                    if r < n:
                        if board[k][r] == 'Q':
                            diag = True
                            break
                        r += 1
                if diag:
                    continue
                board[row_id][i] = 'Q'
                col_set[i] = 1
                if row_id < n - 1:
                    helper(board, row_id+1, result, col_set)
                else:
                    result.append(board)
                    for row in board:
                        print row
                    print '\n'
                board[row_id][i] = '0'
                del (col_set[i])

        helper(board, 0, self.result, {})

obj = Solution()
obj.solveNQueens(5)


