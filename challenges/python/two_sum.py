#------------------------------------------------#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#------------------------------------------------#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in num_map:
                return [num_map[compliment], i]

            num_map[num] = i


solution_class = Solution()
print("solution: ", solution_class.twoSum([2,7,11,15], 9))
print("solution: ", solution_class.twoSum([3,2,4], 6))
print("solution: ", solution_class.twoSum([3,3], 6))
print("--------------------------")

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6

print("two_sum: ", two_sum(nums1, target1))
print("two_sum: ", two_sum(nums2, target2))
print("two_sum: ", two_sum(nums3, target3))

print("--------------------------")


class TwoSum:
    def __init__(self):
        self.num_map = {}

    def add(self, number: int):
        self.num_map[number] = self.num_map.get(number, 0) + 1

    def find(self, target: int):
        for num in self.num_map:
            complement = target - num
            if complement in self.num_map:
                if complement != num or self.num_map[num] > 1:
                    return [num, complement]
        return None

two_sum.add(2)
two_sum.add(7)
two_sum.add(11)
two_sum.add(15)

result = two_sum.find(9)  # Try to find two numbers that sum to 9
print("TwoSum Class:", result)  # Output: [2, 7]
print("--------------------------")
