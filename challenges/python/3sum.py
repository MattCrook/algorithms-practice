#####################################################################
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#####################################################################

#--------------------------#
# SOLUTION 1

# Approach for this Problem:
# - Sort the input array
# - Initialize a set to store the unique triplets and an output vector to store the final result
# - Iterate through the array with a variable i, starting from index 0.
# - Initialize two pointers, j and k, with j starting at i+1 and k starting at the end of the array.
# - In the while loop, check if the sum of nums[i], nums[j], and nums[k] is equal to 0. If it is, insert the triplet into the set and increment j and decrement k to move the pointers.
# - If the sum is less than 0, increment j. If the sum is greater than 0, decrement k.
# - After the while loop, iterate through the set and add each triplet to the output vector.
# - Return the output vector

# Time complexity: O(n^2 logn) // where n is the size of array
# Sorting takes O(nlogn) time and loop takes O(n^2) time, So the overall time complexity is O(nlogn + n^2 logn) - O(n^2 logn)
#--------------------------#

class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output

solution1 = Solution1()
print(solution1.threeSum([-1,0,1,2,-1,-4]))
print(solution1.threeSum([0,1,1]))
print(solution1.threeSum([0,0,0]))
print("-----------------------")


#---------------------------------#
#---------------------------------#
def threeSum(self, nums):

	res = set()

	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0: 
			n.append(num)
		else:
			z.append(num)

	#2. Create a separate set for negatives and positives for O(1) look-up times
	N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
	if len(z) >= 3:
		res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print("-----------------------")


#---------------------------------#
# BRUTE FORCE
#---------------------------------#
class Solution3:
    def threeSum(self, nums):
        ans=set()
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp=nums[i]+nums[j]+nums[k]
                    if temp==0:
                        ans.add((nums[i],nums[j],nums[k]))
        return ans

solution3 = Solution3()
print(solution3.threeSum([-1,0,1,2,-1,-4]))
print(solution3.threeSum([0,1,1]))
print(solution3.threeSum([0,0,0]))
print("-----------------------")

#---------------------------------#
# OPTIMIZED
#---------------------------------#
class Solution4:
    def threeSum(self, nums):
        ans=set()
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                temp=nums[i]+nums[j]+nums[k]
                if temp==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif temp>0:
                    k-=1
                else:
                    j+=1
        return ans

solution4 = Solution4()
print(solution4.threeSum([-1,0,1,2,-1,-4]))
print(solution4.threeSum([0,1,1]))
print(solution4.threeSum([0,0,0]))
print("-----------------------")
