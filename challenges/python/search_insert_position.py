#------------------------------------------------#
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#------------------------------------------------#

# SIMPLE: Using binary search algorithm
# O(n) complexity though.
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for num in nums:
        if num>=target:
            return nums.index(num)
            break
    else:
        return len(nums)

print("Solution 1:", searchInsert([1,3,5,6], 5))
print("Solution 1:", searchInsert([1,3,5,6], 2))
print("Solution 1:", searchInsert([1,3,5,6], 7))
print("--------------------------")



# SIMPLE: Using binary search algorithm
# O(n) complexity though.
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target <= nums[i]:
                return i

        return len(nums)

solution2 = Solution()
print("Solution 2:", solution2.searchInsert([1,3,5,6], 5))
print("Solution 2:", solution2.searchInsert([1,3,5,6], 2))
print("Solution 2:", solution2.searchInsert([1,3,5,6], 7))
print("--------------------------")



# Using While loop and true binary search algorithm.
# O(log n) complexity
class Solution(object):
    def searchInsert(self, nums, target):
        length = 0
        range = len(nums) - 1
        while length <= range:  # With the while loop we can execute a set of statements as long as a condition is true.
            mid = (length + range) // 2  # getting the middle of where we are in the list
            if nums[mid] < target:  # if the value of mid (middle) is less than the target, then increment length. (shifting it right) (we know if won't be anything less than that in the list so can get rid of all those numbers.)
                length = mid + 1
            elif nums[mid] > target: # if value of mid is less than target, then decrement the range. (shifting left, so while length < range, decreases range, removes all options above that mid.)
                range = mid - 1
            else:
                return mid # else we landed on the target
        return length # return ENDING length, which will be the position where target WOULD be if in the list.

solution3 = Solution()
print("Solution 3:", solution3.searchInsert([1,3,5,6], 5))
print("Solution 3:", solution3.searchInsert([1,3,5,6], 2))
print("Solution 3:", solution3.searchInsert([1,3,5,6], 7))
print("--------------------------")




# Using RECURSION loop and true binary search algorithm.
# O(log n) complexity
def helper(nums, target):
    if len(nums) < 1:
        return 0
    mid = len(nums) // 2
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return mid+1 + helper(nums[mid+1:], target)
    else:
        return helper(nums[:mid], target)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return helper(nums, target)

solution4 = Solution()
print("Solution 4:", solution4.searchInsert([1,3,5,6], 5))
print("Solution 4:", solution4.searchInsert([1,3,5,6], 2))
print("Solution 4:", solution4.searchInsert([1,3,5,6], 7))
print("--------------------------")
