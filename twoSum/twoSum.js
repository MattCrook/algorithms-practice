//**************************************************************//
/*
One of the many popular algorithms is the Two Sum Algorithm.
Given an array of numbers and a stand alone number, return all combinations of numbers in the array that add up to the stand alone number.
Although any approach that works is technically a solve, but Big O determines which is the best answer for your application.

Take the following example:

let array = [2,5,8,3,-2,9,0]
let targetSum = 3

- The array of numbers we’re working with is 2,5,8,3,-2,9,0.
- We need to find the number combinations that we’ll equal 3, our “targetSum”.
*/
//**************************************************************//

//******************** BRUTE FORCE ************************//
// A naive approach to this problem would be to loop through each number
// and then loop again through the array looking for a pair that sums to "target_sum".
// The running time for the below solution would be O(n2) because in the worst case we are looping through the array twice to find a pair.
//************************//
function twoSumBruteForce(arr, target_sum) {
  var sums = [];

  // check each element in array
  for (var i = 0; i < arr.length; i++) {
    // check each other element in the array
    for (var j = i + 1; j < arr.length; j++) {
      // determine if these two elements sum to target_sum
      if (arr[i] + arr[j] === target_sum) {
        sums.push([arr[i], arr[j]]);
      }
    }
  }

  // return all pairs of integers that sum to S (7)
  return sums;
}

console.log(twoSumBruteForce([3, 5, 2, -4, 8, 11], 7));
console.log("------------------");

//************************** HashTable/ HashMap **********************//
//   - (2) Solutions here, each with a slightly different way of checking if number,
//   - exists in the HashTable to find a matching pair.
//     - First with converting the type to String.
//     - Second using the "in" operator for JS objects.
//
/*
We can write a faster algorithm that will find pairs that sum to target_sum in linear time.
The algorithm below makes use of hash tables which have a constant lookup time.
As we pass through each element in the array, we check to see if S minus the current element exists in the hash table.
We only need to loop through the array once, resulting in a running time of O(n) since each lookup and insertion in a hash table is O(1).

(1) The hash table is initially empty and the first element in the array is 4.
  - We simply put 4 into the hash table.
(2) The next element is 5.
  - We check to see if the sum minus the current element exists in the hash table. 6 - 5 = 1 does not exist in the hash table. 
  - So add 5 to the hash table.
(3) The next element is 1.
  - We check to see if the sum minus the current element exists in the hash table. 6 - 1 = 5 does exist in the hash table so we found a pair.
*/
//*****************************************************//
function twoSumHashTable(arr, target_sum) {
  var sums = [];
  var hashTable = {};

  // check each element in array
  for (var i = 0; i < arr.length; i++) {
    // calculate S - current element
    var sumMinusElement = target_sum - arr[i];

    // check if this number exists in hash table
    // if so then we found a pair of numbers that sum to S
    if (hashTable[sumMinusElement.toString()] !== undefined) {
      sums.push([arr[i], sumMinusElement]);
    }

    // add the current number to the hash table
    hashTable[arr[i].toString()] = arr[i];
  }

  // return all pairs of integers that sum to S
  return sums;
}

console.log(twoSumHashTable([4, 5, 1, 8], 6));
console.log("----------------");

// *************** //
function twoSumHashTable_2(arr, target) {
  const hashMap = {};
  let pairs = [];

  for (let i = 0; i < arr.length; i++) {
    const compliment = target - arr[i];
    if (compliment in hashMap) {
      pairs.push([arr[i], compliment]);
    }
    hashMap[arr[i]] = arr[i];
  }

  return pairs;
}

console.log(twoSumHashTable_2([4, 5, 1, 8], 6));
console.log("----------------");

// ********** Another way Using HashMap/ HashTable (and ES6 arrow function) *********//
//   - Note - Returns INDEX(s) of matches in the array, rather than the numbers themselves.
// ***************************************************************************//
const twoSumHashmap = (numbers, target) => {
  // Create oject to hold the pair ids
  //  - we will be checking against this object
  // - checking if our target minus the current pair id is in this object, otherwise adding it.
  const hashTable = {}; // numberPairIds

  // Array to hold the Indexes of the pairs we found.
  let pairIndexes = [];

  // For loop to loop through the array of numbers passed in.
  for (let i = 0; i < numbers.length; i++) {
    // saving off value of current iteration, in numbers array.
    const num = numbers[i];
    // Calculating the complement of the current number.
    const compliment = target - num;
    // - For example: 9(target) - 2(num) = 7(compliment).
    //  - 7 is then added to hashTable{}
    //   - this continues, adds the num (2) to the hashTable{}, at index i.
    //   - Until the calculated compliment (7 for example) is found.
    if (compliment in hashTable) {
      // if compliment (7) is found in hashTable{}, return the current index(i), and the index at which it found the compliment(numberPairIds[compliment]).
      pairIndexes.push([i, hashTable[compliment]]);
    }
    // property assignment to hashTable{object}
    // adding the current iteration (i), to hashTable{object} with key hashTable[num].
    // - using bracket ("[]"") property assignment b/c in JS have to if using dynamic property names (e.g., variables) or property names that are not valid JavaScript identifiers (e.g numbers..)
    //   - for example, if hashTable = {}, num = 2, i = 0
    //     - hashTable[num] = i ==> hashTable = {2 : 0}}
    hashTable[num] = i;
  }
  return pairIndexes;
};

console.log("solution: ", twoSumHashmap([2, 7, 11, 15], 9));
console.log("solution: ", twoSumHashmap([3, 2, 4], 6));
console.log("solution: ", twoSumHashmap([3, 3], 6));
console.log("--------------------------");

//*************************************************//
// Class object with same solutions as above.
// Just added together under a Class for conciseness.
//*************************************************//
class TwoSum {
  bruteForce(arr, target_sum) {
    let sums = [];
    for (let i = 0; i < arr.length; i++) {
      for (let j = i + 1; j < arr.length; j++) {
        if (arr[i] + arr[j] === target_sum) {
          sums.push([arr[i], arr[j]]);
        }
      }
    }
    return sums;
  }

  hashTable(arr, target_sum) {
    let sums = [];
    let hashTable = [];
    for (let i = 0; i < arr.length; i++) {
      let num = arr[i];
      let compliment = target_sum - num;
      if (hashTable[compliment.toString()] !== undefined) {
        sums.push([arr[i], compliment]);
      }
      hashTable[num.toString()] = num;
    }
    return sums;
  }

  hashTable_2(arr, target_sum) {
    const hashMap = {};
    let pairs = [];

    for (let i = 0; i < arr.length; i++) {
      const compliment = target_sum - arr[i];
      if (compliment in hashMap) {
        pairs.push([arr[i], compliment]);
      }
      hashMap[arr[i]] = arr[i];
    }

    return pairs;
  }

  pairIndexes(arr, target_sum) {
    const numberPairIds = {};
    let pairIndexes = [];
    for (let i = 0; i < arr.length; i++) {
      const num = arr[i];
      const compliment = target_sum - num;
      if (compliment in numberPairIds) {
        pairIndexes.push([i, numberPairIds[compliment]]);
      }
      numberPairIds[num] = i;
    }
    return pairIndexes;
  }
}

const array = [2, 5, 8, 3, -2, 9, 0];
const targetSum = 3;

const twoSum = new TwoSum();
console.log("Brute Force: ", twoSum.bruteForce(array, targetSum)); // [ [ 5, -2 ], [ 3, 0 ] ]
console.log("Hash Table", twoSum.hashTable(array, targetSum)); // [ [ -2, 5 ], [ 0, 3 ] ]
console.log("Hash Table 2", twoSum.hashTable_2(array, targetSum)); // [ [ -2, 5 ], [ 0, 3 ] ]
console.log("Matching Pairs Induces", twoSum.pairIndexes(array, targetSum)); // [ [ 4, 1 ], [ 6, 3 ] ]
console.log("--------------------------");

// ****************************************************************** //
/*
TWO SUM II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
- Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
// ****************************************************************** //
*/

// ************** SOLUTION #1 ******************* //
// - Two Sum Using the two-pointer method.
// ******************** //
const twoSumTwoPointer = (numbers, target) => {
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
};

console.log(twoSumTwoPointer([2, 7, 11, 15], 9));
console.log(twoSumTwoPointer([2, 3, 4], 6));
console.log(twoSumTwoPointer([-1, 0], -1));
console.log("---------------------");

// ****************** Solution 2 ****************//
// - Two Sum Using an Object (dictionary) to store values we've already calculated (memoization).
// ******************************************* //
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
