
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
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

nums_1 = [2,7,11,15]
target_1 = 9

nums_2 = [3,2,4]
target_2 = 6

nums_3 = [3,3]
target_3 = 6


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            temp = target - nums[i]
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == temp:
                    return [i + 1, mid + 1]
                elif nums[mid] < temp:
                    left = mid + 1
                else:
                    right = mid -1

    def twoSum2(self, nums, target):
        visited = {}
        len_numbers = len(nums)
        for i in range(len_numbers):
            num = nums[i]
            guess = target - num
            if guess in visited:
                indexI = visited[guess][0] + 1
                indexJ = i + 1
                return [indexI, indexJ]
            if num not in visited:
                visited[num] = [i]
            else:
                visited[num] += [i]

        return []

solution = Solution()

print("twoSum 1: ", solution.twoSum(nums_1, target_1))
print("twoSum 2: ", solution.twoSum(nums_2, target_2))
print("twoSum 3: ", solution.twoSum(nums_3, target_3))
print("--------------------------")
print("twoSum 1: ", solution.twoSum2(nums_1, target_1))
print("twoSum 2: ", solution.twoSum2(nums_2, target_2))
print("twoSum 3: ", solution.twoSum2(nums_3, target_3))
