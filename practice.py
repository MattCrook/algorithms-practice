# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.



# nums1 = [3,2,2,3]
# val1 = 3
nums2 = [0,1,2,2,3,0,4,2]
numstwo = [0,1,2,2,3,0,4,2] # [0,1,3,0,4,2]

val2 = 2

class Solution(object):
    def removeElement1(self, nums, val):
      for i in nums:
        if i == val:
          nums.pop(i)
      return nums

    def removeElement(self, nums, val):
      i = 0
      while i < len(nums):
        if nums[i] == val:
          nums.pop(i)
        else:
          i += 1
      return nums




print("original", nums2)
s = Solution()
print(s.removeElement1([0,1,2,2,3,0,4,2], 2)) # [0,1,3,0,4,2]
print(s.removeElement([0,1,2,2,3,0,4,2], 2)) # [0, 1, 0, 4, 2]
