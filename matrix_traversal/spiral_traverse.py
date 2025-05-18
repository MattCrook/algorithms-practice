###################################################################
# Spiral Matrix Traversal
#
# Problem Description: Given a 2D matrix, return its elements in spiral order.
# Algorithm:
#  Initialize variables top, bottom, left, and right to track the boundaries of the matrix.
#  While top <= bottom and left <= right:
#  Traverse from left to right along the top row and increment top.
#  Traverse from top to bottom along the right column and decrement right.
#  If there are remaining rows, traverse from right to left along the bottom row and decrement bottom.
#  If there are remaining columns, traverse from bottom to top along the left column and increment left.
###################################################################

def spiral_traverse(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(spiral_traverse(matrix))
print("-------------------")
