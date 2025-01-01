// ------------------------------- BUBBLE SORT ALGORITHM --------------------------------- //
/*
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted,
compares each pair of adjacent items and swaps them if they are in the wrong order (ascending or descending arrangement).
The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

Bubble Sort is a simple, in-place sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.
- It has a time complexity of O(n²) in the worst case and best case O(n) when the array is already sorted.
- While not the most efficient for large datasets, it's useful for small arrays or when you need a very simple sorting algorithm.

Time Complexity:
- Best Case (O(n)): The best case occurs when the array is already sorted. In this case, the inner loop performs no swaps, and the algorithm terminates after one pass.
- Average and Worst Case (O(n²)): In the worst case, when the array is in reverse order, the algorithm needs to perform n passes, and in each pass, it performs up to n comparisons, resulting in O(n²) time complexity.
Space Complexity:
- O(1): Bubble Sort is an in-place sorting algorithm. It only requires a constant amount of additional memory regardless of the input size.
*/
// -------------------------------------------------------------------------------- //

const bubbleSort = (inputArr) => {
  let len = inputArr.length;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (inputArr[j] > inputArr[j + 1]) {
        let tmp = inputArr[j];
        inputArr[j] = inputArr[j + 1];
        inputArr[j + 1] = tmp;
      }
    }
  }
  return inputArr;
};

let arr = [1, 4, 6, 2, 6, 7, 10];
console.log("------------ bubbleSort ---------");
console.log("Arr initial", arr);
console.log("Arr Sorted:", bubbleSort(arr));
console.log(" ");

// ------ Using a do/ while loop ------ //
const bubbleSortDoWhile = (inputArr) => {
  let len = inputArr.length;
  let swapped;
  do {
    swapped = false;
    for (let i = 0; i < len; i++) {
      if (inputArr[i] > inputArr[i + 1]) {
        let tmp = inputArr[i];
        inputArr[i] = inputArr[i + 1];
        inputArr[i + 1] = tmp;
        swapped = true;
      }
    }
  } while (swapped);
  return inputArr;
};

let arr2 = [1, 4, 6, 2, 6, 7, 10];
console.log("------------ bubbleSortDoWhile ---------");
console.log("Arr initial", arr2);
console.log("Arr Sorted:", bubbleSortDoWhile(arr2));
console.log(" ");

// ------ Practical ES6 way using the sort method ------/
const bubbleSortArrayMethod = (arr) => {
  arr.sort((a, b) => a - b);
  return arr;
};

let arr3 = [1, 4, 6, 2, 6, 7, 10];
console.log("------------ bubbleSortArrayMethod ---------");
console.log("Arr initial:", arr3);
console.log("Arr Sorted:", bubbleSortArrayMethod(arr3));
console.log(" ");

// ---------- Additional Bubble Sort Method ------ //
const bubbleSort_2 = (arr) => {
  const n = arr.length;

  // Outer loop to traverse the entire array
  for (let i = 0; i < n - 1; i++) {
    let swapped = false;

    // Inner loop to perform the comparison and swapping
    for (let j = 0; j < n - i - 1; j++) {
      // Compare adjacent elements
      if (arr[j] > arr[j + 1]) {
        // Swap if they are in the wrong order
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // Swap using destructuring
        swapped = true;
      }
    }

    // If no elements were swapped in this pass, the array is sorted
    if (!swapped) {
      break;
    }
  }
}

const arr4 = [38, 27, 43, 3, 9, 82, 10];
console.log("------------ bubbleSort_2 ---------");
console.log("Arr initial", arr4);
bubbleSort_2(arr4);
console.log("Arr Sorted:", arr4);
console.log(" ");
