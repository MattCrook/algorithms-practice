// ------------------------------- SELECTION SORT ALGORITHM --------------------------------- //
/*
Selection Sort is a simple comparison-based sorting algorithm that works by repeatedly finding the minimum (or maximum) element from the unsorted part of the list and swapping it with the first unsorted element. 
It works by reducing the unsorted portion of the array step by step.
- It uses in-place sorting, meaning the algorithm sorts the array in place without needing extra memory
- it is non-stable meaning that it may change the relative order of equal elements
- The algorithm always performs O(n²) comparisons, regardless of the input's order.
*/
// ------------------------------------------------------------------------------------------ //

// --------- Sorting an Array in Ascending Order --------- //
/*
Suppose you have the following unsorted array: [64, 25, 12, 22, 11]

Time Complexity:
 - Best, Worst, and Average Case: O(n²), where n is the number of elements in the array.
 - Space Complexity: O(1), since it only requires a constant amount of extra space for swaps.

- First Pass (i = 0):
 - Find the minimum element from the unsorted part: [64, 25, 12, 22, 11]
 - The minimum element is 11.
 - Swap 11 with the first element (64).

- Second Pass (i = 1):
 - Find the minimum element from the unsorted part: [25, 12, 22, 64]
 - The minimum element is 12.
 - Swap 12 with the second element (25).

- Third Pass (i = 2):
 - Find the minimum element from the unsorted part: [25, 22, 64]
 - The minimum element is 22.

- Fourth Pass (i = 3):
 - Find the minimum element from the unsorted part: [25, 64]
 - The minimum element is 25, which is already in place.
 - No swap needed.

- Fifth Pass (i = 4):
 - The last element is already in its correct position.
 - No further swaps needed.
*/
// ------------------------------------------------ //
const selectionSortSimple = (arr) => {
  let n = arr.length;

  // Traverse through all array elements
  for (let i = 0; i < n; i++) {
    // Find the minimum element in remaining unsorted array
    let minIndex = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }

    // Swap the found minimum element with the first element
    if (minIndex !== i) {
      let temp = arr[i];
      arr[i] = arr[minIndex];
      arr[minIndex] = temp;
    }
  }

  return arr;
};

let arr = [64, 25, 12, 22, 11];
console.log("Sorted Array: ", selectionSortSimple(arr));
console.log("---------------");

// ------------- Selection Sort: Floating Point Numbers --------- //
// Same Selection Sort algorithm applied to a new array with floating-point values.
// Time Complexity:
//  - Best, Worst, and Average Case: O(n²), where n is the number of elements in the array.
//  - Space Complexity: O(1), as it uses a constant amount of extra space for the swap operation.
// ------------------------------------------------------------- //
function selectionSortFloatingPoint(arr) {
  let n = arr.length;

  for (let i = 0; i < n; i++) {

    let minIndex = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }

    if (minIndex !== i) {
      let temp = arr[i];
      arr[i] = arr[minIndex];
      arr[minIndex] = temp;
    }
  }

  return arr;
}

let arrFloatingPoint = [3.14, 2.71, 1.41, 4.67, 0.577];
console.log("Sorted Array Floating Point:", selectionSortFloatingPoint(arrFloatingPoint));
console.log("---------------");
