// #################################################################### //
/*
Given a sorted array of numbers, determine if a number exists.

Input : sorted = [0, 1, 1, 2, 5, 7, 9, 9, 10], find if these exist [5, 3, 8, 7]
Output: [y, n, n, y]
*/
// #################################################################### //


// ------------------------- SOLUTION #1 ----------------//
// Essentially a Helper function that will be called for each number in the
// search list, and perform a binary search to see if in the sorted list.
// -----------------------------------//
const binSearch = (arr, target) => {
  let min = 0;
  let max = arr.length - 1;
  while (min <= max) {
    let mid = Math.floor((min + max) / 2);
    if (arr[mid] === target) {
      return true;
    } else if (arr[mid] < target) {
      min = mid + 1;
    } else {
      max = mid - 1;
    }
  }
  return false;
};

// Returns a list/array of strings of "Y" or N", of the results of if number is in list.
//  - Ex) ['Y', 'N', 'N', 'Y']
//  - Uses above helper function to perform binary search for each target in the search list.
const doBinarySearch = (arr, targets) => {
  let results = [];
  for (let target of targets) {
    if (binSearch(arr, target)) {
      results.push("Y")
    } else {
      results.push("N");
    }
  }
  return results;
};

console.log("Sol 1: ",doBinarySearch([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7]));
console.log("---------------")


//-------------------- SOLUTION 02 -------------------//
// Solution combining what was the helper function and "main" function
// in the previous examples.
//
// The function checks each number from the target_list against the sorted_array using binary search.
// It efficiently returns "y" for found numbers and "n" for missing numbers.
//--------------------------------------------//
const checkNumbersInSortedArray = (arr, targetList) => {
  const binarySearch = (arr, target) => {
    let min = 0;
    let max = arr.length - 1;
    while (min <= max) {
      let mid = Math.floor((min + max) / 2);
      if (arr[mid] === target) {
        return true;
      } else if (arr[mid] < target) {
        min = mid + 1;
      } else {
        max = mid - 1;
      }
    }
    return false;
  };

  const results = [];

  for (let target of targetList) {
    if (binarySearch(arr, target)) {
      results.push("Y")
    } else {
      results.push("N")
    }
  }
  return results;
}

console.log("Sol 2: ",checkNumbersInSortedArray([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7]));
console.log("---------------")

//-------------------- SOLUTION 03: RECURSION -------------------//
// Using method of Solution #2 of combining into (1) Function.
// But solving Binary Search using a recursive function.
//-------------------------------------------------------//
const checkNumbersInSortedArrayRecursion = (arr, targetList) => {
  const binarySearchRec = (arr, target, min, max) => {
    if (min > max) return false;
    let mid = Math.floor((min + max) / 2);
    if (arr[mid] === target) return true;
    if (arr[mid] < target) {
      return binarySearchRec(arr, target, mid + 1, max)
    } else {
      return binarySearchRec(arr, target, min, mid -1)
    }

  };

  const results = [];

  for (let target of targetList) {
    if (binarySearchRec(arr, target, 0, arr.length - 1)) {
      results.push("Y")
    } else {
      results.push("N")
    }
  }
  return results;
}

console.log("Sol 3: ",checkNumbersInSortedArrayRecursion([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7]));
console.log("---------------")
