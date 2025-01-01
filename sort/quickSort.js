// ------------------------------- QUICK SORT ALGORITHM --------------------------------- //
/*
Quick Sort is another divide - and - conquer algorithm.
It works by selecting a pivot element from the array and partitioning the other elements into two subarrays—those less than the pivot and those greater than the pivot.
These subarrays are then sorted recursively.


Time Complexity:
  - Best case: O(n log n) — Occurs when the pivot divides the array into roughly equal halves.
  - Average case: O(n log n) — Most typical cases where the pivot performs well.
  - Worst case: O(n²) — Occurs when the pivot is always the smallest or largest element (e.g., when the array is already sorted or nearly sorted).
Space Complexity:
  - O(log n) for the recursive stack in the best and average cases.
  - O(n) in the worst case for the recursion stack.

Summary:
- Quick Sort is generally faster than other O(n log n) algorithms (like Merge Sort) in practice due to smaller constant factors and better cache performance.
- The worst-case time complexity of O(n²) can be avoided with random pivot selection or using techniques like median-of-three to choose the pivot.
*/
// ----------------------------------------------------------------------------------- //

function quickSort(arr) {
  // Base case: if the array has one or zero elements, it's already sorted
  if (arr.length <= 1) {
    return arr;
  }

  // Step 1: Choose a pivot element (Here, we choose the last element)
  const pivot = arr[arr.length - 1];
  const left = [];
  const right = [];

  // Step 2: Partition the array into two subarrays
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  // Step 3: Recursively sort the left and right subarrays, then combine with the pivot
  return [...quickSort(left), pivot, ...quickSort(right)];
}

const arr = [38, 27, 43, 3, 9, 82, 10];
const sortedArr = quickSort(arr);
console.log("Sorted array:", sortedArr);
console.log("---------------------");

// ------------------------------ Quick Sort (In-place with Lomuto Partition Scheme) ------------------------ //
/*
Another way to inpliment this algorithm, the array is modified in place without needing additional arrays(left and right).
The idea is to choose a pivot and rearrange the array such that all elements smaller than the pivot come before it, and all elements greater than the pivot come after it.
Then, the same process is recursively applied to the left and right subarrays.

This is an in-place Quick Sort implementation using Lomuto’s partition scheme. 
- It avoids the extra space used for creating new subarrays by partitioning the array directly. 
- While Quick Sort is very efficient in practice (on average, O(n log n)), it can degrade to O(n²) in the worst case if the pivot selection is poor. 
- To mitigate this, variations like randomized Quick Sort or median-of-three pivot selection can be used.
*/
// -------------------------------------------------------------------------------------------//

function quickSortInPlace(arr, low = 0, high = arr.length - 1) {
  if (low < high) {
    // Step 1: Find the pivot index
    const pivotIndex = partition(arr, low, high);

    // Step 2: Recursively sort the subarrays
    quickSortInPlace(arr, low, pivotIndex - 1); // Left subarray
    quickSortInPlace(arr, pivotIndex + 1, high); // Right subarray
  }
}

// Lomuto partition scheme
function partition(arr, low, high) {
  const pivot = arr[high]; // Choose the last element as pivot
  let i = low - 1; // Pointer for the smaller element

  // Step 1: Rearrange elements so that smaller ones go to the left
  for (let j = low; j < high; j++) {
    if (arr[j] < pivot) {
      i++;
      // Swap arr[i] and arr[j]
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  // Step 2: Place the pivot in the correct position
  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];

  // Return the index of the pivot
  return i + 1;
}

// Example usage
const arrInPlace = [38, 27, 43, 3, 9, 82, 10];
console.log("(Initial) Array (in place):", arrInPlace);
quickSortInPlace(arr);
console.log("(Sorted) Array (in place):", arrInPlace);
console.log("---------------------");


// ------------------------------ Quick Sort Algorithm Using Hoare's Partition Scheme ------------------- //
/*
Note - this scheme still Sorts In Place.

- In Hoare's partition scheme, we select a pivot element (typically the first element),
- and partition the array by moving two pointers toward each other—one from the left looking for an element greater than the pivot and one from the right looking for an element smaller than the pivot. 
- These two elements are swapped.
- This continues until the pointers cross, at which point the pivot is placed in its correct position.

Time Complexity:
  - Best case: O(n log n) — This occurs when the pivot divides the array into nearly equal parts.
  - Average case: O(n log n) — Most common case when the pivot divides the array reasonably well.
  - Worst case: O(n²) — This occurs when the pivot is always the smallest or largest element (e.g., if the array is already sorted or nearly sorted).
Space Complexity:
  - O(log n) for the recursion stack in the best and average cases (logarithmic depth of recursion).
  - O(n) for the recursion stack in the worst case (if the array is already sorted or nearly sorted).

Why Hoare's Partition Scheme is Better:
  - Fewer swaps: Hoare's partitioning scheme typically requires fewer swaps than Lomuto's partition scheme, as it only performs a swap when the pointers i and j are out of order.
  - More efficient: Since the pointers move towards each other from both ends, fewer elements need to be moved around, making the partitioning process more efficient.
This version of Quick Sort is often faster in practice, especially for large arrays, due to fewer swaps and a more efficient partitioning process.
*/
// ------------------------------------------------------------------------------------------- //
function quickSortHoare(arr, low = 0, high = arr.length - 1) {
  if (low < high) {
      // Step 1: Partition the array and get the pivot index
      const pivotIndex = hoarePartitionScheme(arr, low, high);

      // Step 2: Recursively sort the left and right subarrays
      quickSort(arr, low, pivotIndex);    // Left subarray (including pivot)
      quickSort(arr, pivotIndex + 1, high);  // Right subarray (excluding pivot)
  }
}

function hoarePartitionScheme(arr, low, high) {
  const pivot = arr[low];  // Choose the first element as the pivot
  let i = low - 1;
  let j = high + 1;

  while (true) {
      // Move `i` to the right, looking for an element greater than the pivot
      do {
          i++;
      } while (arr[i] < pivot);

      // Move `j` to the left, looking for an element smaller than the pivot
      do {
          j--;
      } while (arr[j] > pivot);

      // If the pointers have crossed, return the partition index
      if (i >= j) {
          return j;
      }

      // Swap elements at `i` and `j`
      [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}


const arrHoare = [38, 27, 43, 3, 9, 82, 10];
console.log("(Initial) Array", arrHoare)
quickSortHoare(arrHoare);
console.log("Sorted array (Hoares Partition Scheme) In place:", arrHoare);
console.log("------------------")
