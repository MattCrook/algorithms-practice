//-----------------------------------------------//
// Search the array of prime numbers for a given value using a binary search
//-----------------------------------------------//

const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];


function doSearch(array, targetValue) {
  // looking for the index of our target value
  // min is starting point
  // max is the length of array or total number of induces
  // guess is current index number in the array
  // array[guess] is the index value
  let min = 0;
  let max = array.length - 1;
  let guess;
  while (min <= max) {
    // while we are still looping through the array...or while we havnt reached the max or end of array
    // guess equals the closest integer rounded down, find the index
    // guess starts as the halfway point index of the array
    guess = Math.floor((max + min) / 2);
    // if it finds the index, return true
    // else look to the left or right accordingly
    if (array[guess] === targetValue) {
      return guess;
    } else if (array[guess] < targetValue) {
      // if the starting index is less than our target value, than we dont need all the numbers below it.
      // new min is current array[guess] or (the index number) 1 greater than current value, and look to the right.
      min = guess + 1;
    } else {
      // else if the targetVal is greater than the current index, disregard all the numbers to the right and new index is one to down to the left .
      max = guess - 1;
    }
  }
  // if it doesn't find it return false.
  return -1;
}
console.log("doSearch", doSearch(primes, 73));



// Using Recursion
function binaryRecursion(arr, targetValue, min, max) {
  if (min > max) return false;
  let middleIndex = Math.floor((max + min) / 2);
  if (arr[middleIndex] === targetValue) return middleIndex;
  if (arr[middleIndex] > targetValue) {
    return binaryRecursion(arr, targetValue, min, middleIndex - 1);
  } else {
    return binaryRecursion(arr, targetValue, middleIndex + 1, max);
  }
}

console.log("doSearchRecursion", binaryRecursion(primes, 73, 0, primes.length - 1));
