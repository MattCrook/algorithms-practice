/*
------------------------------------------------
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 You may assume that each input would have exactly one solution, and you may not use the same element twice.
 You can return the answer in any order.

 Example 1:

 Input: nums = [2,7,11,15], target = 9
 Output: [0,1]
 Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

 Example 2:
 Input: nums = [3,2,4], target = 6
 Output: [1,2]

 Example 3:
 Input: nums = [3,3], target = 6
 Output: [0,1]
------------------------------------------------
*/

// Using HASHMAP solution
function twoSumHashmap(numbers, target) {
  // Create oject to hold the pair ids
  //  - we will be checking against this object
  // - checking if our target minus the current pair id is in this object, otherwise adding it. 
  const numberPairIds = {};

  // For loop to loop through the array of numbers passed in.
  for (let i = 0; i < numbers.length; i++) {
    // saving off value of current iteration, in numbers array.
    const num = numbers[i];
    // Calculating the complement of the current number.
    const compliment = target - num;
    // - For example: 9(target) - 2(num) = 7(compliment).
    //  - 7 is then added to numberPairIds{}
    //   - this continues, adds the num (2) to the numberPairIds{}, at index i.
    //   - Until the calculated compliment (7 for example) is found.
    if (compliment in numberPairIds) {
      // if compliment (7) is found in numberPairIds{}, return the current index(i), and the index at which it found the compliment(numberPairIds[compliment]).
      return [i, numberPairIds[compliment]];
    }
    // property assignment to numberPairIds{object}
    // adding the current iteration (i), to numberPairIds{object} with key numberPairIds[num].
    // - using bracket ("[]"") property assignment b/c in JS have to if using dynamic property names (e.g., variables) or property names that are not valid JavaScript identifiers (e.g numbers..)
    //   - for example, if numberPairIds = {}, num = 2, i = 0
    //     - numberPairIds[num] = i ==> numberPairIds = {2 : 0}}
    numberPairIds[num] = i;
  }
}

console.log("solution: ", twoSumHashmap([2, 7, 11, 15], 9));
// console.log("solution: ", twoSumHashmap([3, 2, 4], 6));
// console.log("solution: ", twoSumHashmap([3, 3], 6));
console.log("--------------------------");

// Same solution just using ES6 arrow function syntax.
const twoSum = (nums, target) => {
  const dict = {}
  for (let i in nums) {
    const number = nums[i];
    if (target - number in dict) {
      return [i, dict[target - number]]
    }
    dict[number] = i;
  }
}

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
console.log("--------------------------");
