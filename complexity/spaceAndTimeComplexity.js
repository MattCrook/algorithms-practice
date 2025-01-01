/*
SUMMARY

Time Complexity
- Time complexity is concerned with how the running time of an algorithm or function grows as the size of the input increases. 
- We analyze the time complexity by counting the number of basic operations or steps the function performs, and then express that in Big-O notation.

Steps to analyze time complexity:
- Identify the Input Size:
  - The input size n is usually the number of elements that the algorithm operates on. For example, for a list of numbers, n is the number of elements in the list.
  - Break the function into parts:
    - For loops, recursive calls, function calls, etc., all contribute to the overall time complexity. You need to carefully examine how many times these parts are executed.

- Determine dominant terms:
  - In most cases, you focus on the term with the highest growth rate. For instance:
    - A single loop over n elements results in O(n).
    - A nested loop over n elements results in O(n²).
    - A recursive function with halving input size results in O(log n).

- Simplify to Big-O notation:
  - The Big-O notation is used to express the upper bound of time complexity.
  - After counting operations, express the complexity in terms of the most significant term.

Space Complexity
- Space complexity is concerned with how much memory (space) an algorithm uses as a function of the input size.
- This includes the space used by variables, data structures, function call stacks, and so on.

- Steps to analyze space complexity:
  - Identify the space used by input:
    - Space complexity typically depends on how much extra space is used relative to the input size. Space used by the input itself is generally not counted unless we modify it.
  - Account for all variables and data structures:
    - Consider any additional space used by arrays, hash maps, stacks, or other data structures within the function.
  - Consider recursion:
    - If the function is recursive, space complexity can be affected by the call stack. Each recursive call adds a new layer to the stack, and in some cases, this contributes to space complexity.
  - Simplify to Big-O notation:
    - Just like time complexity, space complexity is often simplified to Big-O notation.


Measuring Time and Space Complexity:

Time Complexity:
- O(1): Constant time (e.g., accessing an element in an array).
- O(n): Linear time (e.g., iterating over an array).
- O(n²): Quadratic time (e.g., nested loops).
- O(log n): Logarithmic time (e.g., binary search).
- O(n log n): Linearithmic time (e.g., merge sort).

Space Complexity:
- O(1): Constant space (e.g., using only a few variables).
- O(n): Linear space (e.g., creating a new array of size n).
- O(n) (recursion): Space used by the call stack in recursion.


In summary:
- Time complexity is measured by counting the number of operations relative to the input size.
- Space complexity is measured by considering how much extra memory the function uses.
*/


// ################## Time Complexity ################ //

// ----------- Constant Time O(1) ----------- //
// - An operation with O(1) time complexity means that no matter how large the input is, the time taken will always be constant.
// - Accessing a single element
// - Accessing an element by index in an array is a constant-time operation, meaning it doesn't depend on the size of the array.
// ------------------------------------------- //
function constantTimeExample(arr) {
  return arr[0];
}

console.log("constantTimeExample: ", constantTimeExample([1, 2, 3, 4, 5])); // Output: 1
console.log("----------------")

// ------------ Linear Time O(n) ------------ //
// - An operation with O(n) time complexity means that the time taken grows linearly with the input size.
// - (Printing each element)
// - This function loops over every element in the array, so the time taken is directly proportional to the size of the array (n), hence O(n).
// ------------------------------------------- //
function linearTimeExample(arr) {
  for (let i = 0; i < arr.length; i++) {
    return arr[i];
  }
}

console.log("linearTimeExample: ", linearTimeExample([1, 2, 3, 4, 5]));
console.log("----------------")
/*
Output:
1
2
3
4
5
*/

// ---------- Quadratic Time O(n²) ---------- //
// - An operation with O(n²) time complexity involves two nested loops that both depend on the input size.
// - (Printing each pair of elements)
// - The outer loop runs n times, and for each iteration of the outer loop, the inner loop runs n times as well. So, the time complexity is O(n²).
// ------------------------------------------- //
function quadraticTimeExample(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      console.log(arr[i], arr[j]);
    }
  }
}

console.log("quadraticTimeExample: ")
quadraticTimeExample([1, 2, 3]);
console.log("----------------")
/* Output will include all pairs of elements:
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
*/

// -------- Logarithmic Time O(log n) --------- //
// An operation with O(log n) time complexity means that the problem is divided in half (or some other fraction) with each iteration, like in binary search.
// The value of i doubles each time, so the number of iterations is proportional to the logarithm of n. This gives us O(log n) time complexity.
// ------------------------------------------- //
function logarithmicTimeExample(n) {
  let i = 1;
  while (i < n) {
    console.log(i); // Log value of i
    i *= 2; // Double i each time
  }
}

console.log("logarithmicTimeExample: ")
logarithmicTimeExample(16);
console.log("----------------")
/* Output:
1
2
4
8
*/

// --------- Linearithmic Time O(n log n) ---------- //
// - Common algorithms like Merge Sort and Quick Sort have O(n log n) time complexity because they divide the problem recursively (log n) and then combine the results (linear n).
// - The merge sort algorithm splits the array in half each time, and the merging step takes linear time. 
// - Thus, the time complexity is O(n log n).
// ------------------------------------------- //
function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

function merge(left, right) {
  let result = [];
  let i = 0,
    j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }

  return result.concat(left.slice(i), right.slice(j));
}

console.log("linearithmicTimeMergeSortExample: ", mergeSort([5, 3, 8, 1, 2, 7]));
console.log("----------------")

// ################### Space Complexity ###################### //

// ---------------- Constant Space O(1) -------- //
// - An algorithm has O(1) space complexity when it uses a constant amount of extra space, regardless of the input size.
// - The function only uses a few variables (sum, i) and no extra data structures that depend on the size of the input. Thus, space complexity is O(1).
// ------------------------------------------- //
function constantSpaceExample(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]; // Only a few variables are used
  }
  return sum;
}

console.log("constantSpaceExample: ", constantSpaceExample([1, 2, 3, 4])); // Output: 10
console.log("----------------")


// --------------- Linear Space O(n) ---------- //
// - An algorithm has O(n) space complexity when it uses space proportional to the size of the input.
// - The function creates a new array result that is the same size as the input array arr, so space complexity is O(n).
// ------------------------------------------- //
function linearSpaceExample(arr) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(arr[i] * 2); // Create a new array
  }
  return result;
}

console.log("linearSpaceExample: ", linearSpaceExample([1, 2, 3])); // Output: [2, 4, 6]
console.log("----------------")


// --------- Space Complexity with Recursion --------- //
// - Recursive functions use space for each recursive call in the call stack, which contributes to space complexity.
// - Each recursive call adds a new layer to the call stack, and the depth of the recursion is n. Therefore, the space complexity is O(n), because there are n function calls in the stack.
// ------------------------------------------------ //

function recursiveFactorial(n) {
  if (n <= 1) return 1;
  return n * recursiveFactorial(n - 1);
}

console.log("recursiveFactorial: ", recursiveFactorial(5)); // Output: 120
console.log("----------------")
