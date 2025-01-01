// ------------------------------- HEAP SORT ALGORITHM --------------------------------- //
/*
Heap Sort is a comparison-based sorting algorithm that takes advantage of a binary heap data structure to efficiently sort an array or list. 
It works by first transforming the list into a max-heap or a min-heap, and then repeatedly extracting the largest (or smallest) element to build the sorted array.

Key Concepts:
- A heap is a special tree-based data structure that satisfies the heap property:
- In a max-heap, the value of each node is greater than or equal to the values of its children.
- In a min-heap, the value of each node is smaller than or equal to the values of its children.
- Heap Sort typically uses a max-heap to sort the elements in ascending order.
- The largest element is always at the root of the heap (top of the tree), so it can be moved to the end of the array.
- After extracting the root, the heap property is restored, and the process continues.
How Heap Sort Works:
- Build a Max Heap: The first step is to turn the input array into a max-heap. In a max-heap, the largest element is at the root.
- Extract the Maximum Element: The root element (which is the maximum in a max-heap) is swapped with the last element in the array. After the swap, the heap size is reduced by one, and the heap property is restored by "heapifying" the root.
- Repeat: This process is repeated for the remaining heap (with one less element each time) until the heap size becomes 1.
Time Complexity:
- Best, Average, Worst Case: O(n log n)
Space Complexity: O(1) — Heap Sort is an in-place sorting algorithm.
- Stable: Heap Sort is not stable, meaning that it does not necessarily preserve the order of equal elements from the input array.


Time Complexity:
- Building the heap takes O(n) time since each call to initHeap operates in O(log n), and there are n/2 nodes to call initHeap on.
- Extracting elements: Each extraction takes O(log n) because the initHeap function runs in O(log n), and we do this n-1 times (since the last element is already sorted).
Therefore, the overall time complexity is O(n log n), which holds for the best, average, and worst cases.

Space Complexity:
O(1): Heap Sort is an in-place sorting algorithm, meaning it does not require additional space apart from the input array itself, except for the recursive stack in the worst case.

Why Heap Sort?
- Efficient: Heap Sort has a guaranteed O(n log n) time complexity, which makes it a good alternative to other sorting algorithms, especially for large datasets.
- In-place: It doesn’t require additional memory for another array, making it more memory-efficient compared to algorithms like Merge Sort.
- Non-stable: Heap Sort is not stable, meaning that it does not guarantee to preserve the relative order of equal elements in the sorted array.

Heap Sort is a very efficient sorting algorithm with a guaranteed time complexity of O(n log n).
- It is an in-place, non-stable sorting algorithm that uses a binary heap to efficiently find the largest element and place it in its correct position. 
- It is particularly useful in situations where space complexity is a critical factor, but the lack of stability might be a downside for some use cases.
*/
// ----------------------------------------------------------------------------------- //
function initHeap(arr, n, i) {
  let largest = i;  // Initialize largest as root
  let left = 2 * i + 1;  // Left child index
  let right = 2 * i + 2;  // Right child index

  // If left child is larger than root
  if (left < n && arr[left] > arr[largest]) {
      largest = left;
  }

  // If right child is larger than root
  if (right < n && arr[right] > arr[largest]) {
      largest = right;
  }

  // If largest is not root, swap and "heapify" the affected subtree
  if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]];  // Swap
      initHeap(arr, n, largest);  // Recursively "heapify" the affected subtree
  }
}


function heapSort(arr) {
  const n = arr.length;

  // Step 1: Build a max heap
  // Start from the last non-leaf node and move upwards
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    initHeap(arr, n, i);
  }

  // Step 2: Extract elements from the heap one by one
  for (let i = n - 1; i > 0; i--) {
      // Swap the root (max) element with the last element
      [arr[0], arr[i]] = [arr[i], arr[0]];

      // Reduce the heap size and restore the heap property
      initHeap(arr, i, 0);
  }
}


const arr = [38, 27, 43, 3, 9, 82, 10];
heapSort(arr);
console.log("Sorted array:", arr);
console.log("-------------------")
