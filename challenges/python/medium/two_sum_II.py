#------------------------------------------------#
# Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
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
    # two-pointer
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
        """
        O(n(log(n)) time complexity and O(1) space
        """
        n = len(numbers)
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if numbers[i] + numbers[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
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


#------------------------------------------------#
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
# #------------------------------------------------#

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
        visited = {}
        len_numbers = len(numbers)

        for i in range(len_numbers):
            num = numbers[i]
            guess = target - num
            if guess in visited:
                indexI = visited[guess] + 1
                indexJ = i + 1
                return [indexI, indexJ]
            if num not in visited:
                visited[num] = [i]
            else:
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


#------------------------------------------------#
# Another way to do it with binary search
#------------------------------------------------#
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

solution_3 = Solution_3()
print(solution_3.twoSum([2, 7, 11, 15], 9));
print(solution_3.twoSum([2,3,4], 6));
print(solution_3.twoSum([-1, 0], -1));
