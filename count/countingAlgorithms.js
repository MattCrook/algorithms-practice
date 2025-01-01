// ------------------------------ COUNTING ALGORITHMS -------------------------------------- //
// Counting algorithms are algorithms used to determine the frequency or count of specific elements, typically in a collection or dataset. These algorithms can be used to track occurrences, frequencies, or even to help solve more complex problems like sorting or histogram generation.

// Summary
//   - Counting Sort: Sorts an array by counting occurrences of each element.
//   - Frequency Count (Hash Map): Tracks how many times each element appears in an array using a hash map.
//   - Bucket Sort: Distributes elements into buckets, then sorts and concatenates them.
//   - Histogram Counting: Tracks the frequency distribution of data into bins.
//   - Radix Sort: Sorts using digit-based counting sort as a subroutine.
//   - Kadane's Algorithm: Finds the maximum sum of a contiguous subarray in O(n) time.

// These algorithms are often used in different scenarios based on the problem domain, such as sorting, frequency analysis, or optimization problems.
// ------------------------------------------------------------------------------ //

// ---------------- Counting Sort Algorithm --------------- //
// Counting Sort is an efficient algorithm for sorting when the range of input values is known and is not significantly greater than the number of elements. It works by counting the number of occurrences of each value in the array, then using that information to place each element in its correct position.

// Time Complexity: O(n + k), where:
// n is the number of elements in the array.
// k is the range of the input (maximum element value).
// Space Complexity: O(k) for the auxiliary array used for counting.
// -------------------------------------------------------- //
function countingSort(arr) {
  const max = Math.max(...arr); // Find the max value in the array
  const count = new Array(max + 1).fill(0); // Create count array

  // Count occurrences of each element
  for (let i = 0; i < arr.length; i++) {
    count[arr[i]]++;
  }

  // Rebuild the sorted array
  let index = 0;
  for (let i = 0; i < count.length; i++) {
    while (count[i] > 0) {
      arr[index++] = i;
      count[i]--;
    }
  }
  return arr;
}

const arr = [4, 2, 2, 8, 3, 3, 1];
console.log(countingSort(arr)); // Output: [1, 2, 2, 3, 3, 4, 8]

// ---------------- Frequency Count (Hash Map) -------------- //
// A frequency count algorithm counts the occurrences of each unique element in a dataset using a hash map (or hash table) to store the count. It is widely used for counting occurrences of elements in arrays or lists.
//   - Time Complexity: O(n), where n is the number of elements in the array.
//   - Space Complexity: O(n) for the hash map storage.
// -------------------------------------------------------- //
function frequencyCount(arr) {
  const countMap = {};
  for (let i = 0; i < arr.length; i++) {
    countMap[arr[i]] = (countMap[arr[i]] || 0) + 1;
  }
  return countMap;
}

const arr2 = [1, 2, 2, 3, 3, 3, 4];
console.log(frequencyCount(arr2)); // Output: { '1': 1, '2': 2, '3': 3, '4': 1 }

// --------------Bucket Counting (Bucket Sort) ----------- //
// Bucket Sort works by distributing the elements of the input array into a number of buckets, counting the elements in each bucket, and then sorting the elements of each bucket individually. It's commonly used when the elements are uniformly distributed over a range.
//   - Time Complexity: O(n + k), where n is the number of elements and k is the number of buckets (typically close to n).
//   - Space Complexity: O(n + k)
// -------------------------------------------------------- //
function bucketSort(arr) {
  const n = arr.length;
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const bucketCount = Math.floor((max - min) / n) + 1;
  const buckets = new Array(bucketCount).fill().map(() => []);

  // Distribute elements into buckets
  for (let i = 0; i < n; i++) {
    const index = Math.floor((arr[i] - min) / n);
    buckets[index].push(arr[i]);
  }

  // Sort each bucket and concatenate the result
  return buckets.flat().sort((a, b) => a - b);
}

const arr3 = [0.42, 0.32, 0.23, 0.53, 0.91];
console.log(bucketSort(arr3)); // Output: [0.23, 0.32, 0.42, 0.53, 0.91]

// -------------------- Histogram Counting ----------------------- //
// A histogram is a representation of the frequency distribution of a dataset. It counts how many times values fall within specified ranges or bins. This can be useful in data analysis, particularly for understanding the distribution of continuous data.
//   - Time Complexity: O(n), where n is the number of data points.
//   - Space Complexity: O(k), where k is the number of bins.
// -------------------------------------------------------- //
function createHistogram(arr, binSize) {
  const histogram = {};

  // Count occurrences in bins
  for (let i = 0; i < arr.length; i++) {
    const bin = Math.floor(arr[i] / binSize) * binSize;
    histogram[bin] = (histogram[bin] || 0) + 1;
  }
  return histogram;
}

const data = [1, 2, 2, 8, 3, 9, 10, 11, 12];
console.log(createHistogram(data, 5)); // Output: { '0': 3, '5': 3, '10': 3 }

// ----------------- Radix Sort (Counting Sort as a Subroutine) ---------- //
// Radix Sort is a non-comparative sorting algorithm that sorts numbers (or strings) digit by digit, from the least significant digit to the most significant (or vice versa). It uses counting sort as a subroutine to sort the digits.
//   - Time Complexity: O(nk), where n is the number of elements and k is the number of digits (or character length).
//   - Space Complexity: O(n + k)
// -------------------------------------------------------- //
function countingSortForRadix(arr, exp) {
  const n = arr.length;
  const output = new Array(n);
  const count = new Array(10).fill(0);

  // Count occurrences
  for (let i = 0; i < n; i++) {
    const index = Math.floor(arr[i] / exp) % 10;
    count[index]++;
  }

  // Calculate positions
  for (let i = 1; i < 10; i++) {
    count[i] += count[i - 1];
  }

  // Build the output array
  for (let i = n - 1; i >= 0; i--) {
    const index = Math.floor(arr[i] / exp) % 10;
    output[count[index] - 1] = arr[i];
    count[index]--;
  }

  // Copy the output to arr
  for (let i = 0; i < n; i++) {
    arr[i] = output[i];
  }
}

function radixSort(arr) {
  const max = Math.max(...arr);

  // Apply counting sort for every digit
  for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10) {
    countingSortForRadix(arr, exp);
  }

  return arr;
}

const arr4 = [170, 45, 75, 90, 802, 24, 2, 66];
console.log(radixSort(arr4)); // Output: [2, 24, 45, 66, 75, 90, 170, 802]

// ------------------- Kadanes' Algorithm for Maximum Subarray Sum -------------- //
// Though not strictly a "counting" algorithm, Kadane's algorithm is often considered in the context of counting contiguous subarrays and their sums. It is used to find the maximum sum of a contiguous subarray within a one-dimensional numeric array.
//   - Time Complexity: O(n)
//   - Space Complexity: O(1)
// ---------------------------------------------------------------- //
function maxSubArraySum(arr) {
  let maxSoFar = arr[0];
  let maxEndingHere = arr[0];

  for (let i = 1; i < arr.length; i++) {
    maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
    maxSoFar = Math.max(maxSoFar, maxEndingHere);
  }

  return maxSoFar;
}

const arr5 = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
console.log(maxSubArraySum(arr5)); // Output: 6 (Subarray: [4, -1, 2, 1])
