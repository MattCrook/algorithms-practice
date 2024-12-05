
#------------------------------------------------#
# Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
# #------------------------------------------------#

class Solution(object):
  def twoSum(self, numbers, target):
    n = len(numbers)
    for i in range(n):
      left = i + 1
      right = n - 1
      # if numbers[i] + numbers[right] == target:
      #   return [numbers[i], numbers[right]]
      while left < right:
        mid = (left + right) // 2
        if numbers[mid] + numbers[i] >= target:
          right = mid
        else:
          left = mid + 1
        if numbers[left] + numbers[i] == target:
          return [i + 1, left + 1]

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9));
print(solution.twoSum([2,3,4], 6));
print(solution.twoSum([-1, 0], -1));
