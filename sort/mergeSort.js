// ------------------------------- MERGE SORT ALGORITHM --------------------------------- //
/*
Merge Sort is a divide-and-conquer algorithm.
It works by dividing the array into two halves, sorting each half recursively, and then merging the sorted halves.

Steps:
  - Divide the unsorted list into two halves.
  - Recursively sort each half.
  - Merge the two sorted halves to produce the final sorted list.

Example Explanation:
  - mergeSort(arr) function:
    - This function splits the input array into two halves recursively until each half contains one or zero elements.
    - The array is divided by finding the middle index (mid), and two subarrays (leftHalf and rightHalf) are created using slice().
    - The function recursively calls itself on the left and right subarrays, then merges them using the merge() function.
  - merge(left, right) function:
    - This function merges two sorted arrays (left and right) into one sorted array.
    - It compares the elements of the left and right arrays and adds the smaller element to the sortedArray.
    - After one array is exhausted, the remaining elements of the other array are appended to the sortedArray.

Time Complexity:
  - Best case: O(n log n)
  - Average case: O(n log n)
  - Worst case: O(n log n)
*/
// ------------------------------------------------------------------------------------- //

function mergeSort(arr) {
  // Base case: if the array has 1 or 0 elements, it's already sorted
  if (arr.length <= 1) {
    return arr;
  }

  // Step 1: Split the array into two halves
  const mid = Math.floor(arr.length / 2);
  const leftHalf = arr.slice(0, mid);
  const rightHalf = arr.slice(mid);

  // Step 2: Recursively sort each half
  return merge(mergeSort(leftHalf), mergeSort(rightHalf));
}

// Function to merge two sorted arrays
function merge(left, right) {
  let sortedArray = [];
  let i = 0;
  let j = 0;

  // Compare elements from left and right and build the sorted array
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      sortedArray.push(left[i]);
      i++;
    } else {
      sortedArray.push(right[j]);
      j++;
    }
  }

  // If there are remaining elements in the left array, add them
  if (i < left.length) {
    sortedArray = sortedArray.concat(left.slice(i));
  }

  // If there are remaining elements in the right array, add them
  if (j < right.length) {
    sortedArray = sortedArray.concat(right.slice(j));
  }

  return sortedArray;
}

const arr = [38, 27, 43, 3, 9, 82, 10];
const sortedArr = mergeSort(arr);
console.log("Sorted array:", sortedArr); //Output => Sorted array: [3, 9, 10, 27, 38, 43, 82]
console.log("------------------------");

// ------------------------------ Iterative Merge Sort (Bottom-Up Approach) ------------------------ //
/*
Merge Sort algorithm splits the array and recursively sorts the halves, an alternative approach can be to implement it iteratively using bottom-up merging. 
This avoids recursion and uses a non-recursive approach to merge subarrays in a bottom-up manner.
  - In the iterative approach, the idea is to iteratively merge pairs of subarrays. 
  - Initially, the subarrays have size 1, then progressively double the size of the subarrays being merged until the entire array is merged.

Time Complexity:
  - Best case: O(n log n)
  - Average case: O(n log n)
  - Worst case: O(n log n)
Space Complexity:
  - O(n): The iterative version still requires extra space for the temporary subarrays (leftArr and rightArr), so the space complexity is O(n).
*/
// -------------------------------------------------------------------------------------------//
function mergeSortIterative(arr) {
  let n = arr.length;

  // Start with subarrays of size 1
  let size = 1;

  // Keep doubling the subarray size
  while (size < n) {
    // Merge subarrays in pairs of the current size
    for (let left = 0; left < n; left += 2 * size) {
      // Find the end of the right subarray and the mid-point
      let mid = Math.min(n, left + size);
      let right = Math.min(n, left + 2 * size);

      // Merge the two sorted subarrays
      mergeIterative(arr, left, mid, right);
    }
    size *= 2; // Double the size of subarrays for the next iteration
  }

  return arr;
}

// Function to merge two sorted subarrays
function mergeIterative(arr, left, mid, right) {
  // Create temporary arrays to hold the left and right subarrays
  let leftArr = arr.slice(left, mid);
  let rightArr = arr.slice(mid, right);

  let i = 0,
    j = 0,
    k = left;

  // Merge the two subarrays
  while (i < leftArr.length && j < rightArr.length) {
    if (leftArr[i] <= rightArr[j]) {
      arr[k++] = leftArr[i++];
    } else {
      arr[k++] = rightArr[j++];
    }
  }

  // Copy any remaining elements from the left array
  while (i < leftArr.length) {
    arr[k++] = leftArr[i++];
  }

  // Copy any remaining elements from the right array
  while (j < rightArr.length) {
    arr[k++] = rightArr[j++];
  }
}

const arrIterative = [38, 27, 43, 3, 9, 82, 10];
const sortedArrIterative = mergeSortIterative(arr);
console.log("Sorted array iterative:", sortedArrIterative);
console.log("------------------------------------");
