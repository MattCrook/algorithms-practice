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

  // return all pairs of integers that sum to S
  return sums;
}

console.log(twoSumBruteForce([3, 5, 2, -4, 8, 11], 7));
console.log("------------------");

//************** HashTable/ HashMap **********************//
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
//************************//
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

// ********** Another way Using HashMap/ HashTable (and ES6 arrow function) *********//
// *******************************//
const twoSumHashmap = (numbers, target) => {
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
};

console.log("solution: ", twoSumHashmap([2, 7, 11, 15], 9));
console.log("solution: ", twoSumHashmap([3, 2, 4], 6));
console.log("solution: ", twoSumHashmap([3, 3], 6));
console.log("--------------------------");
