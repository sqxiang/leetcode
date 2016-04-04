class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        L = len(matrix)
        R = (L + 1) // 2
        for x in range(0, R):
            for y in range(0, L - R):
                #(x,y)->(y,l-1-x)->(l-1-x,l-1-y)->(l-1-y,x)
                matrix[x][y], matrix[y][L-1-x], matrix[L-1-x][L-1-y], matrix[L-1-y][x] \
                = matrix[L-1-y][x], matrix[x][y], matrix[y][L-1-x], matrix[L-1-x][L-1-y]
        return matrix

solution = Solution()
print solution.rotate([[1]])