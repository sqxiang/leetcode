class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r,l,m = [],[],[]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in r:
                        print 'board[i][j]',board[i][j]
                        r.append(board[i][j])
                    else:
                        return False
                if board[j][i]!='.':
                    if board[j][i] not in l:
                        print 'board[j][i]',board[j][i]
                        l.append(board[j][i])
                    else:
                        return False
                if board[j/3+i/3*3][j%3+i%3*3]!='.':
                    if board[j/3+i/3*3][j%3+i%3*3] not in m:
                        print 'board[j/3+i/3*3][j%3+i%3*3]',board[j/3+i/3*3][j%3+i%3*3]
                        m.append(board[j/3+i/3*3][j%3+i%3*3])
                    else:
                        return False
                if j == 8:
                    r,l,m = [],[],[]
        return True

solution = Solution()
print solution.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])