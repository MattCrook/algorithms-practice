/*
#########################################################
THREE SUM

(Also see /challenges/ folder for more examples.)
#########################################################
*/

//------------ BRUTE FORCE ------------------//
// When approaching an algorithms problem, particularly when thinking about the brute force approach,
// it is often easiest to start by thinking about how you would solve a given problem if you were to solve it by hand.
//
// While the answer for this example input may be obvious by simply looking at the array and thinking about the problem,
// you could also solve it by generating all the possible triplet combinations and evaluating which triplets meet the required criteria A + B + C = 0.
//
// Time/Space Complexity
// - Time Complexity: O(n²)
// - Space Complexity: O(n²)
//-----------------------------------------//
const threeSumBruteForce = (nums) => {
  const threeSums = {};
  for (let i = 0; i <= nums.length; i++) {
    for (let j = i; j <= nums.length; j++) {
      for (let k = j; k <= nums.length; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
          const sortedNums = [nums[i], nums[j], nums[k]].sort();
          threeSums[`${sortedNums}`] = sortedNums;
        }
      }
    }
  }
  return Object.values(threeSums);
};

console.log(threeSumBruteForce([7, 4, -7, 0]));
console.log("------------------");

/*
//------------ (BETTER SOLUTION) USING HASHMAP ------------------//
Time/Space Complexity
 - Time Complexity: O(n²)
 - Space Complexity: O(n²)
//-------------------------------------------------------------//
 */
const twoSumsMapper = (nums) => {
  const twoSumsMap = {};
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const twoSum = nums[i] + nums[j];
      if (!twoSumsMap[twoSum]) {
        twoSumsMap[twoSum] = new Set();
      }
      const sortedTuple = [nums[i], nums[j]].sort();
      twoSumsMap[twoSum].add(sortedTuple);
    }
  }
  return twoSumsMap;
};
const countOccurrences = (nums) => {
  return nums.reduce((acc, cv) => {
    if (acc[cv]) {
      acc[cv] += 1;
    } else {
      acc[cv] = 1;
    }
    return acc;
  }, {});
};
const threeSumHashMap = (nums) => {
  const twoSumMap = twoSumsMapper(nums);
  const counterForNums = countOccurrences(nums);
  const threeSums = {};
  for (let i = 0; i <= nums.length; i++) {
    // looking for two numbers that sum to the inverse of the current value
    const twoSumTuplesForValue = twoSumMap[-nums[i]] || new Set();
    for (const [numOne, numTwo] of twoSumTuplesForValue) {
      if ((nums[i] !== numOne && nums[i] !== numTwo) || counterForNums[nums[i]] >= 3) {
        const sortedNums = [nums[i], numOne, numTwo].sort();
        threeSums[`${sortedNums}`] = sortedNums;
      }
    }
  }
  return Object.values(threeSums);
};

console.log(threeSum([7, 4, -7, 0]));
console.log("------------------");

//----------------- SORTING, ITERATING, AND TWO POINT--------------//
// In this case we can design an algorithm that combines both of the approaches above. 
// - We first sort the array, then iterate over it (index I), placing two pointers (L and R) at the beginning and end of the other already-sorted numbers.
// - To iterate the two pointers, we can conditionally moving either the left or right pointer based on whether the current triplet sum is larger or smaller than zero. 
// - If at any point arr[I] + arr[L] + arr[R] = 0 that means we have found a triplet that sums to zero.
//
// Consider the following array: [-2, 3, 1, 7, -4, 9]
// And the same array sorted: [-4, -2, 1, 3, 7, 9]
// When iterating over an array we should also pause to consider whether adding a second pointer, known as the "two pointers" approach, would be helpful.
//
// Time/Space Complexity
// - Time Complexity: O(n²)
// - Space Complexity: O(n) (or O(1) if sorted in-place)
//-------------------------------------------------------------//
const threeSum = (nums) => {
  const sortedNums = nums.sort((a, b) => a - b);
  const threeSums = [];
  for (let i = 0; i < nums.length; i++) {
    // avoid duplicates
    if (i > 0 && sortedNums[i] === sortedNums[i - 1]) {
      continue;
    }
    const target = -sortedNums[i];
    let [l, r] = [i + 1, sortedNums.length - 1];
    while (l < r) {
      if (sortedNums[l] + sortedNums[r] === target) {
        threeSums.push([sortedNums[i], sortedNums[l], sortedNums[r]]);
        l += 1;
        // avoid duplicates again
        while (l < r && sortedNums[l] === sortedNums[l - 1]) {
          l += 1;
        }
      } else if (sortedNums[l] + sortedNums[r] < target) {
        l += 1;
      } else {
        r -= 1;
      }
    }
  }
  return threeSums;
};

console.log(threeSum([7, 4, -7, 0]))
console.log(threeSum([-4, -2, 1, 3, 7, 9]))
console.log("-------------------")
