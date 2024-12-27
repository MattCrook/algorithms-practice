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
const array = [2, 5, 8, 3, -2, 9, 0];
const targetSum = 3;

function twoSumBruteForce(arr, target_sum) {
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

//console.log(twoSumBruteForce(array, targetSum));

const twoSum = (arr, target) => {
  const hashMap = {}
  let pairs = [];
  for (let i = 0; i < arr.length; i++) {
    const compliment = target - arr[i];
    if (compliment in hashMap) {
      pairs.push([arr[i], compliment])
    }
    hashMap[arr[i]] = arr[i];
  }
  return pairs;
};

console.log(twoSum(array, targetSum));
