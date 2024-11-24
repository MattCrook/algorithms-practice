# ~ using to traverse by matrix antidiagonal (the second diagonal)


class Solution:
    def diagonalSum(self, matrix):
        result = 0
        for i in range(len(matrix)):
            result = result + matrix[i][i] + matrix[i][~i]

        if (len(matrix)) % 2:
            mid = len(matrix)//2
            result -= matrix[mid][mid]

        return result

s = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(s.diagonalSum(matrix))
