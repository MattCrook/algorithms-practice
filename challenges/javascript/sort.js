//---------------------------------------------------------------//
// Sort the Array of numbers.

// Do one example mutating the original Array.
// Do another returning a new array that is a sorted copy of the first.
//---------------------------------------------------------------//

let arr = [1, 4, 6, 2, 6, 7, 10];
let arr2 = [1, 4, 6, 2, 6, 7, 10];
let arr3 = [1, 4, 6, 2, 6, 7, 10];

const sortArray = (inputArr) => {
  inputArr.sort((a, b) => a - b);
  return inputArr;
};

sortArray(arr);
console.log("original arr now sorted: ", arr);
console.log("-------");

const sortArrayNoMutateOriginal = (inputArr) => {
  newArr = [...inputArr];
  newArr.sort((a, b) => a - b);
  return newArr;
};

console.log("new shallow copy of arr but sorted: ", sortArrayNoMutateOriginal(arr2));
console.log("original arr: ", arr2);
console.log("-------");

//---------------------//
// Using Bubble Sort Algorithm
//  - Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted,
//  - and compares each pair of adjacent items and swaps them if they are in the wrong order (ascending or descending arrangement).
//  - The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
// Note  - this also mutates the original array.
//---------------------//
function bubbleSort(inputArr) {
  let len = inputArr.length;
  // Iterate over the array's induces
  for (i = 0; i < len; i++) {
    // For each index, iterate over the entire array again
    for (j = 0; j < len; j++) {
      // if value of the current index (inputArr[j]) is greater than the value of the next immediate index (inputArr[j + 1])
      if (inputArr[j] > inputArr[j + 1]) {
        // Then, swap it for that immediate next index.
        let currentIndexValue = inputArr[j];
        inputArr[j] = inputArr[j + 1];
        inputArr[j + 1] = currentIndexValue;
        // it will continue to do this for the length of the array ([i])
        // So that by time we get to the end, (the length), we have checked all indices and sorted in ascending order.
      }
    }
  }
  return inputArr;
}

console.log("bubbleSort: ", bubbleSort(arr3));
console.log("-------");
