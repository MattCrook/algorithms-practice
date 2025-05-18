/*
One of the many popular algorithms is the Two Sum Algorithm.
Given an array of numbers and a stand alone number, return all combinations of numbers in the array that add up to the stand alone number.
Although any approach that works is technically a solve, but Big O determines which is the best answer for your application.

*/

var a = [3, 5, 2, -4, 8, 11];
var target = 7;

const twoSum = (arr, targetSum) => {
  const hashTable = {};
  const pairIndexes = [];
  for (let i = 0; i < arr.length; i++) {
    const number = arr[i];
    const compliment = target - number;
    if (compliment in hashTable) {
        pairIndexes.push([i, hashTable[compliment]]);
    }
    hashTable[number] = i;
  }
  return pairIndexes;
}

console.log(twoSum(a, target));

const twoSumHashTable_2 = (arr, target) => {
    const hashTable = {};
    const pairs = [];
    for (let i = 0; i < arr.length; i++){
        const number = arr[i];
        const complement = target - number;
        if (complement in hashTable) {
            pairs.push([number, complement])
        }
        console.log(hashTable)
        hashTable[number] = arr[i]
    }
    return pairs;

  }
  
  console.log(twoSumHashTable_2(a, target));
  console.log("----------------");
