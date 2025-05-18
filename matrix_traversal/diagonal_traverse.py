###################################################################
# Diagonal Matrix Traversal
# Problem Description: Traverse a matrix diagonally starting from the top-right corner to the bottom-left corner.
#   Algorithm:
#   Traverse the upper half of the matrix (including the diagonal).
#   For each diagonal, start at (0, d) where  d is the column index.
#   Move downwards and leftwards until you reach the bottom or left boundary.
#   Then traverse the lower half starting from (d, n-1) where d is the row index.
###################################################################

def diagonal_traverse(matrix):
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    for d in range(n):
        row, col = 0, d
        while row < m and col >= 0:
            result.append(matrix[row][col])
            row += 1
            col -= 1

    for d in range(1, m):
        row, col = d, n - 1
        while row < m and col >= 0:
            result.append(matrix[row][col])
            row += 1
            col -= 1

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(diagonal_traverse(matrix))
print("-------------------")
