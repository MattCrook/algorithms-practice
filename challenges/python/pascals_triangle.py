#--------------------------------------------------------#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it: as shown:
#
#             1
#           1   1
#         1   2   1
#       1   3   3   1
#     1   4   6   4   1
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#--------------------------------------------------------#

#--------- Using Recursion ----------#
class Solution(object):
    def generate(self, numRows: int):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows

        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

        prevRows.append(newRow)
        return prevRows


solution_1 = Solution()
print("solution_1", solution_1.generate(5))
print("solution_1", solution_1.generate(1))
print("--------------------------")


#--------- Using Combinatorial Formula ---------#
class Solution_02:
    def generate(self, numRows: int):
        result = []
        if numRows == 0:
            return result

        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result

solution_2 = Solution_02()
print("solution_2", solution_2.generate(5))
print("solution_2", solution_2.generate(1))
print("--------------------------")

#---------- Using Dynamic Programming with 1D Array ---------#
class Solution_3:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]

        for i in range(1, numRows - 1):
            current_row.append(prev_row[i - 1] + prev_row[i])

        current_row.append(1)
        prev_rows.append(current_row)

        return prev_rows


solution_3 = Solution_3()
print("solution_3", solution_3.generate(5))
print("solution_3", solution_3.generate(1))
print("--------------------------")
