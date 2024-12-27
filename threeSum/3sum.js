// ######################################################### //
/*
THREE SUM

The Three Sum problem involves finding unique triplets of numbers in an array that sum up to a given target. 
Solve it efficiently by building on top of the Two Sum problem and applying sorting and hashing approaches. 


- Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
- Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
*/
// ######################################################### //

//------------ SOLUTION #1 - BRUTE FORCE ------------------//
// When approaching an algorithms problem, particularly when thinking about the brute force approach,
// it is often easiest to start by thinking about how you would solve a given problem if you were to solve it by hand.
//
// While the answer for this example input may be obvious by simply looking at the array and thinking about the problem,
// you could also solve it by generating all the possible triplet combinations and evaluating which triplets meet the required criteria A + B + C = 0.
//
// Time/Space Complexity
// - Time Complexity: O(n²)
// - Space Complexity: O(n²)
//------------------------------------------------------//
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

console.log("threeSumBruteForce: ", threeSumBruteForce([7, 4, -7, 0]));
console.log("------------------");

//------------ SOLUTION #2 (BETTER SOLUTION) USING HASHMAP ---------//
//Time/Space Complexity
// - Time Complexity: O(n²)
// - Space Complexity: O(n²)
//-------------------------------------------------------------//
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

console.log("threeSumHashMap: ", threeSumHashMap([7, 4, -7, 0]));
console.log("------------------");

//-------- SOLUTION #3 - SORTING, ITERATING, AND TWO POINT --------//
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
const threeSum_3 = (nums) => {
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

console.log("threeSum_3: ", threeSum_3([7, 4, -7, 0]));
console.log("threeSum_3: ", threeSum_3([-4, -2, 1, 3, 7, 9]));
console.log("-------------------");

//-------- SOLUTION #4 SORTING, ITERATING, AND TWO POINT -------//
// -------------------------------------------------------------//

const threeSum_4 = (nums) => {
  const results = [];

  // obviously irrelevant if we don't have at least 3 numbers to play with.
  if (nums.length < 3) return results;

  // having the numbers in ascending order will make this problem much easier.
  // also, knowing the overall problem  will take at least O(N^2) time, we can
  // afford the O(NlogN) sort operation
  nums = nums.sort((a, b) => a - b);

  // if the question asks us for a custom target, we can control it here
  let target = 0;

  for (let i = 0; i < nums.length - 2; i++) {
    // `i` represents the "left" most number in our sorted set.
    // once this number hits 0, there's no need to go further since
    // positive numbers cannot sum to a negative number
    if (nums[i] > target) break;

    // we don't want repeats, so skip numbers we've already seen
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    // `j` represents the "middle" element between `i` and `k`.
    // we will increment this up through the array while `i` and `k`
    // are anchored to their positions. we will decrement `k` for
    // for each pass through the array, and finally increment `i`
    // once `j` and `k` meet.
    let j = i + 1;

    // `k` represents the "right" most element
    let k = nums.length - 1;

    // to summarize our setup, we have `i` that starts at the beginning,
    // `k` that starts at the end, and `j` that races in between the two.
    //
    // note that `i` is controlled by our outer for-loop and will move the slowest.
    // in the meantime, `j` and `k` will take turns inching towards each other depending
    // on some logic we'll set up below. once they collide, `i` will be incremented up
    // and we'll repeat the process.

    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k];

      // if we find the target sum, increment `j` and decrement `k` for
      // other potential combos where `i` is the anchor
      if (sum === target) {
        // store the valid threesum
        results.push([nums[i], nums[j], nums[k]]);

        // this is important! we need to continue to increment `j` and decrement `k`
        // as long as those values are duplicated. in other words, we wanna skip values
        // we've already seen. otherwise, an input array of [-2,0,0,2,2] would result in
        // [[-2,0,2], [-2,0,2]].
        //
        // (i'm not a fan of this part because we're doing a while loop as we're
        // already inside of another while loop...)
        while (nums[j] === nums[j + 1]) j++;
        while (nums[k] === nums[k - 1]) k--;

        // finally, we need to actually move `j` forward and `k` backward to the
        // next unique elements. the previous while loops will not handle this.
        j++;
        k--;

        // if the sum is too small, increment `j` to get closer to the target
      } else if (sum < target) {
        j++;

        // if the sum is too large, decrement `k` to get closer to the target
      } else {
        // (sum > target)
        k--;
      }
    }
  }

  return results;
};

console.log("threeSum_4", threeSum_4([-1, 0, 1, 2, -1, -4]));
console.log("threeSum_4", threeSum_4([0, 1, 1]));
console.log("threeSum_4", threeSum_4([0, 0, 0]));
console.log("------------------");

//----------------- SOLUTION #5 ------------------//
// - Another additional way using sorting, iteration, and two pointer
// -----------------------------------------------//
const threeSum_5 = (nums) => {
  let res = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let j = i + 1;
    let k = nums.length - 1;

    while (j < k) {
      let total = nums[i] + nums[j] + nums[k];

      if (total > 0) {
        k--;
      } else if (total < 0) {
        j++;
      } else {
        res.push([nums[i], nums[j], nums[k]]);
        j++;

        while (nums[j] === nums[j - 1] && j < k) {
          j++;
        }
      }
    }
  }
  return res;
};

console.log("threeSum_5", threeSum_5([-1, 0, 1, 2, -1, -4]));
console.log("threeSum_5", threeSum_5([0, 1, 1]));
console.log("threeSum_5", threeSum_5([0, 0, 0]));
console.log("------------------");

//---- SOLUTION #6 SORTING, ITERATING, AND TWO POINTER ---------//
// - Another additional way using sorting, iteration, and two pointer
// - Almost the same as Solution #4.
//-------------------------------------------------------------//
const threeSum_6 = (nums) => {
  const results = [];
  nums.sort((a, b) => a - b); // Sort the array

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue; // Skip duplicates

    let left = i + 1; // Left pointer
    let right = nums.length - 1; // Right pointer

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        results.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;

        // Skip duplicates
        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      } else if (sum < 0) {
        left++; // Move left pointer to the right to increase the sum
      } else {
        right--; // Move right pointer to the left to decrease the sum
      }
    }
  }

  return results;
};

console.log("threeSum_6", threeSum_6([-1, 0, 1, 2, -1, -4]));
console.log("threeSum_6", threeSum_6([0, 1, 1]));
console.log("threeSum_6", threeSum_6([0, 0, 0]));
console.log("------------------");
