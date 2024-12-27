#--------------------------------------------------------#
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
#--------------------------------------------------------#

#-------- SOLUTION #1 - Simple HashMap--------#
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
print("two_sum 1: ", solution_class.twoSum([2,7,11,15], 9))
print("two_sum 1: ", solution_class.twoSum([3,2,4], 6))
print("two_sum 1: ", solution_class.twoSum([3,3], 6))
print("--------------------------")

#------------ SOLUTION #2 - HashMap -------------#
def two_sum(nums, target):
    # Dictionary to store the number and its index
    num_map = {}
    # Iterate over the list
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        # Check if the complement exists in the map
        if complement in num_map:
            # Return the indices of the complement and the current number
            # pick off the compliment and return the index of that.
            return [num_map[complement], i]
        # Otherwise, store the current number and its index
        num_map[num] = i
    # If no solution is found, return an empty list (this shouldn't happen as per the problem description)
    return []

nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6

print("two_sum 2: ", two_sum(nums1, target1))
print("two_sum 2: ", two_sum(nums2, target2))
print("two_sum 2: ", two_sum(nums3, target3))

print("--------------------------")


#------------ SOLUTION #3 - More involved HashMap -------------#
class TwoSum:
    def __init__(self):
        # Initialize an empty dictionary to store number and its index
        self.num_map = {}

    def add(self, number: int):
        # Store the number and its index in the map
        self.num_map[number] = self.num_map.get(number, 0) + 1

    def find(self, target: int):
        # Iterate over the stored numbers to check for complement
        for num in self.num_map:
            complement = target - num
            # Check if complement exists and is not the same number (or it appears more than once)
            if complement in self.num_map:
                if complement != num or self.num_map[num] > 1:
                    return [num, complement]
        return None

two_sum = TwoSum()  # Instantiate the object
two_sum.add(2)      # Add number 2 to the map
two_sum.add(7)      # Add number 7 to the map
two_sum.add(11)     # Add number 11 to the map
two_sum.add(15)     # Add number 15 to the map

result = two_sum.find(9)  # Try to find two numbers that sum to 9
print("TwoSum 3: ", result)  # Output: [2, 7]
print("--------------------------")


##############################################################
# TWO SUM II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# - Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.


# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
##############################################################

# ---------- SOLUTION #1 ----------- #
# - Two Sum using the two-pointer method.
# - Two Sum using a dictionary (hashmap).
# - (2) examples of Two Sum using a binary search.
# ----------------------------------- #
class Solution(object):
    def twoSumTwoPointer(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

    # dictionary
    def twoSumDictionary(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

    # binary search
    def twoSumBinarySearch(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1

    # binary search #2
    def twoSumBinarySearch2(self, numbers, target):
        "O(n(log(n)) time complexity and O(1) space"
        n = len(numbers)

        for i in range(n):
            # assign vars to left and right values. (min and max)
            #  - ("pythonic"): left, right = i+1, n-1
            # left is min most value we can have (current index of iteration)
            # right is max we can have which is total len of array.
            left = i + 1
            right = n - 1
            # perform binary search
            while left < right:
                # mid is getting the middle or average of array for a starting point
                mid = (left + right) // 2
                # if value at i in numbers, plus value at mid in numbers is greater than our target,
                # then re-assign the right value to mid.
                # B/c, if they don't both add up to target, it is not a match.
                # Therefor if too high, we need to assign mid to lower value, and can disregard anything higher than that.
                if numbers[i] + numbers[mid] >= target:
                    right = mid
                else:
                    # else numbers[i]+numbers[mid] <= than target...
                    # So reassign left to mid. (plus 1, otherwise get stuck in an infinite loop)
                    left = mid + 1
                # final check if value in "numbers" at "left" index plus value at "numbers" at "i" equals our target,
                # return current index "i", and "left", plus 1 per instructions for 1-indexed array.
                if numbers[left] + numbers[i] == target:
                    return [i + 1, left + 1]


solution = Solution()
print(solution.twoSumTwoPointer([2, 7, 11, 15], 9));
print(solution.twoSumTwoPointer([2,3,4], 6));
print(solution.twoSumTwoPointer([-1, 0], -1));
print("-----")
print(solution.twoSumDictionary([2, 7, 11, 15], 9));
print(solution.twoSumDictionary([2,3,4], 6));
print(solution.twoSumDictionary([-1, 0], -1));
print("-----")
print(solution.twoSumBinarySearch([2, 7, 11, 15], 9));
print(solution.twoSumBinarySearch([2,3,4], 6));
print(solution.twoSumBinarySearch([-1, 0], -1));
print("-----")
print(solution.twoSumBinarySearch2([2, 7, 11, 15], 9));
print(solution.twoSumBinarySearch2([2,3,4], 6));
print(solution.twoSumBinarySearch2([-1, 0], -1));
print("----------------------------------")


#------------- SOLUTION #2 -------------#
# Using Hashmap
#
# Approach:
# - Hash Map: Use a dictionary to keep track of the indices of the elements we have seen so far. This allows us to check in constant time whether the complement (i.e., target - num) of the current element exists in the list.
#   - Iterate through the list: As we iterate through the list, for each element, we check if the complement exists in the dictionary. If it does, we have found our pair, and we return their indices. If not, we add the current element and its index to the dictionary.
#   - Return the result: If a pair is found, return their 1-based indices. If not, return an empty list.

# Complexity
# - Time complexity:O(n), where:
#   - n is the length of the input list.
#   - We only iterate through the list once, and each lookup or insertion operation in the hash map is O(1) on average.
# Space complexity:
#   - O(n), as we store up to
#   - n elements in the hash map.
# #-----------------------------------------#
class SolutionHashmap(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        # sorted in non decreasing order
        # 2 number added to specific target
        # indexes + 1
        """
        # Set to hold numbers already visited. Unordered and unique.
        visited = {}
        # number to represent the length of the numbers list passed in.
        len_numbers = len(numbers)

        # simple for loop over range of len_numbers
        # range() function gives a sequence of numbers (starting from 0 by default) and increments by 1 (by default), until a specified number is reached.
        # gives, starting index (0), to last index. (e.g. (0, 4) in first example.)
        for i in range(len_numbers):
            # assigning value of current index in loop to temp var.
            num = numbers[i]
            # assigning what we are looking for to variable...
            # - doing (target - num) b/c math...if the two numbers add up to the target,
            # - then we can assume the target minus the current number equals the other number.
            #   - e.g: 9 - 2 = 7, 9 - 7 = 2...
            guess = target - num
            if guess in visited:
                # first, check to make sure the value (guess) is not already in the Set "visited".
                # if not, then add it to visited, adding the INDEX where it found the match, then plus 1 to adhere to a 1-indexed array.
                # - e.g. in example 1, first past guess = 7 (9 - 2), second pass guess = 2 (9 -7 )
                #   - 7 is in visited, so 2 is a match at first index, so visited[guess] = 0. But + 1 = 1
                indexI = visited[guess] + 1
                indexJ = i + 1
                return [indexI, indexJ]
            if num not in visited:
                # if num (value of current index) not in Set "visited", add it.
                # e.g: visited = {} -> visited = {2: 0}
                visited[num] = [i]
            else:
                # clean up/ edge case num not in visited and haven't found guess
                # increment current value at the current index.
                visited[num] += [i]

        return []

    def twoSumPythonic(self, numbers, target):
        """
        More "pythonic" way / refactored.
        Shorter var names and combined variable declarations.
        """
        visited = {}
        n = len(n)

        for i in range(n):
            num = numbers[i]
            if target - num in visited:
                indexI, indexJ = visited[target - num][-1] + 1, i + 1
                return [indexI, indexJ]
            if num not in visited:
                visited[num] = [i]
            else:
                visited[num] += [i]

        return []

solution_hashmap = SolutionHashmap()
print(solution_hashmap.twoSum([2, 7, 11, 15], 9));
print(solution_hashmap.twoSum([2,3,4], 6));
print(solution_hashmap.twoSum([-1, 0], -1));
print("----")
print(solution_hashmap.twoSumPythonic([2, 7, 11, 15], 9));
print(solution_hashmap.twoSumPythonic([2,3,4], 6));
print(solution_hashmap.twoSumPythonic([-1, 0], -1));
print("---------------------------")


#------------- SOLUTION #3 -------------#
# Another way to do it with binary search
#----------------------------------------#
class Solution_3(object):
    def twoSum(self, array, target):
        i = 0
        j = len(array) -1
        while i < j:
            sum = array[i] + array[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [i+1, j+1]
        return []

solution3 = Solution_3()
print(solution3.twoSum([2, 7, 11, 15], 9));
print(solution3.twoSum([2,3,4], 6));
print(solution3.twoSum([-1, 0], -1));
