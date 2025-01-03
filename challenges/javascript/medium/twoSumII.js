/*
------------------------------------------------
# Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# - Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# - Your solution must use only constant extra space.

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
# #------------------------------------------------
*/

/*
# Solution 2
- Two Sum Using the two-pointer method.
*/
function twoSumTwoPointer(numbers, target) {
  let left = 0;
  let right = numbers.length - 1;
  while (left < right) {
    let sum = numbers[left] + numbers[right];
    if (sum === target) {
      return [left + 1, right + 1]; //return induces added by 1 (per instructions)
    }
    if (sum < target) {
      left = left + 1;
    } else {
      right = right - 1;
    }
  }
}

console.log(twoSumTwoPointer([2, 7, 11, 15], 9));
console.log(twoSumTwoPointer([2, 3, 4], 6));
console.log(twoSumTwoPointer([-1, 0], -1));
console.log("---------------------");

/*
# Solution 2
- Two Sum Using an Object (dictionary)
- to store values we've already calculated (memoization)
*/
const twoSumDictionary = (numbers, target) => {
  const dict = {};
  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];
    const compliment = target - num;
    if (compliment in dict) {
      return [dict[compliment] + 1, i + 1]; //return induces added by 1 (per instructions)
    }
    dict[num] = i;
  }
};

console.log(twoSumDictionary([2, 7, 11, 15], 9));
console.log(twoSumDictionary([2, 3, 4], 6));
console.log(twoSumDictionary([-1, 0], -1));
console.log("---------------------");
