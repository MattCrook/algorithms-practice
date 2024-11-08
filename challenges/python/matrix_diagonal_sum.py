# ~ using to traverse by matrix antidiagonal (the second diagonal)


class Solution:
    def diagonalSum(self, mat):
        res = 0
        for i in range(len(mat)):
            res = res + mat[i][i] + mat[i][~i]

        if (len(mat)) % 2:
            mid = len(mat)//2
            res -= mat[mid][mid]

        return res

s = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(s.diagonalSum(matrix))
