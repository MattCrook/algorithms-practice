#########################################################
# THREE SUM
#
# (Also see /challenges/ folder for more examples.)
#########################################################

#------------ BRUTE FORCE ------------------#
# When approaching an algorithms problem, particularly when thinking about the brute force approach, 
# it is often easiest to start by thinking about how you would solve a given problem if you were to solve it by hand. 
#
# While the answer for this example input may be obvious by simply looking at the array and thinking about the problem, 
# you could also solve it by generating all the possible triplet combinations and evaluating which triplets meet the required criteria A + B + C = 0.
#
# Time/Space Complexity
# - Time Complexity: O(n²)
# - Space Complexity: O(n²)
#-----------------------------------------#
def threeSumBruteForce(nums):
        three_sums = {}
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_answer = sorted([nums[i], nums[j], nums[k]])
                        three_sums[str(sorted_answer)] = [nums[i], nums[j], nums[k]]
        return three_sums.values()

print(threeSumBruteForce([7, 4, -7, 0]))
print("-------------------")


#------------ BETTER SOLUTION USING HASHMAP ------------------#
# Time/Space Complexity
#  - Time Complexity: O(n²)
#  - Space Complexity: O(n²)
#-------------------------------------------------------------#
from collections import defaultdict, Counter

def twoSumsMap(nums):
    two_sums_map = defaultdict(set)
    for i, val_one in enumerate(nums):
        for j, val_two in enumerate(nums[i+1:]):
            two_sums_map[val_one + val_two].add(
                (val_one, val_two)
                if val_one <= val_two else
                (val_two, val_one)
            )
    return two_sums_map

def threeSumHashMap(nums):
    # O(n^2)
    two_sums_map = twoSumsMap(nums)
    # O(n)
    counter_for_nums = Counter(nums)
    three_sums = {}
    # iterating on the dictionary instead of `nums` in order to avoid duplicative work
    for curr_val in counter_for_nums.keys():
        two_sum_tuples_for_val = two_sums_map[-curr_val]
        for val_one, val_two in two_sum_tuples_for_val:
            if (curr_val != val_one and curr_val != val_two) or counter_for_nums[curr_val] >= 3:
                sorted_vals = sorted([curr_val, val_one, val_two])
                three_sums[str(sorted_vals)] = sorted_vals
    return three_sums.values()

print(threeSumHashMap([7, 4, -7, 0]))
print("-------------------")



#----------------- SORTING, ITERATING, AND TWO POINT--------------#
# In this case we can design an algorithm that combines both of the approaches above. 
# - We first sort the array, then iterate over it (index I), placing two pointers (L and R) at the beginning and end of the other already-sorted numbers.
# - To iterate the two pointers, we can conditionally moving either the left or right pointer based on whether the current triplet sum is larger or smaller than zero. 
# - If at any point arr[I] + arr[L] + arr[R] = 0 that means we have found a triplet that sums to zero.
#
# Consider the following array: [-2, 3, 1, 7, -4, 9]
# And the same array sorted: [-4, -2, 1, 3, 7, 9]
# When iterating over an array we should also pause to consider whether adding a second pointer, known as the "two pointers" approach, would be helpful.
#
# Time/Space Complexity
# - Time Complexity: O(n²)
# - Space Complexity: O(n) (or O(1) if sorted in-place)
#-------------------------------------------------------------#
def threeSum(nums):
    sorted_nums = sorted(nums)
    three_sums = []
    for i in range(len(sorted_nums)):
        # avoid duplicates
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue
        target = -sorted_nums[i]
        l, r = i + 1, len(sorted_nums) - 1
        while l < r:
            if sorted_nums[l] + sorted_nums[r] == target:
                three_sums.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                l += 1
                # avoid duplicates again
                while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                    l += 1
            elif sorted_nums[l] + sorted_nums[r] < target:
                l += 1
            else:
                r -= 1
    return three_sums

print(threeSum([7, 4, -7, 0]))
print(threeSum([-4, -2, 1, 3, 7, 9]))
print("-------------------")
