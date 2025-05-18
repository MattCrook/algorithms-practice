###################################################################
# Zigzag Matrix Traversal
#
# Problem Description: Traverse a matrix in a zigzag pattern.
#   Algorithm:
#   Start at the top-left corner.
#   Alternate between moving diagonally up-right and down-left.
#   Adjust direction based on boundary conditions.
###################################################################

def zigzag_traverse(matrix):
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []
    row, col = 0, 0
    going_up = True

    while len(result) < m * n:
        result.append(matrix[row][col])

        if going_up:
            if row > 0 and col < n - 1:
                row -= 1
                col += 1
            else:
                going_up = False
                if col == n - 1:
                    row += 1
                else:
                    col += 1
        else:
            if row < m - 1 and col > 0:
                row += 1
                col -= 1
            else:
                going_up = True
                if row == m - 1:
                    col += 1
                else:
                    row += 1

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(zigzag_traverse(matrix))
print("-------------------")
