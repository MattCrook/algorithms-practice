/* *********************************************************** */
/*
H INDEX

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
- According to the definition of h-index on Wikipedia:
  - The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:
 - Input: citations = [3,0,6,1,5]
 - Output: 3
 - Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
 - Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.Example 2:

Input: citations = [1,3,1]
 - Output: 1
*/
/* *********************************************************** */

const citations01 = [3, 0, 6, 1, 5];
const citations02 = [1, 3, 1];

// ------------ SOLUTION #1 ---------------- //
// ----------------------------------------- //
const hIndex = (citations) => {
  // Sort the citations array:
  // This organizes the citation counts in ascending order, making it easier to check the number of papers with citations ≥ h.
  citations.sort((a, b) => a - b);
  // Initialize and set an initial value for h index to 0.
  let h_index = 0;
  // Iterate through the sorted array:
  //  - For each citation at index i, calculate the number of papers with citations greater than or equal to the current value.
  //  - This is given by citations.length - i.
  for (let i = 0; i < citations.length; i++) {
    // Check two cases:
    //  - If the citation count at the current index (citations[i]) is less than or equal to the number of papers (citations.length - i), update h_ind as the maximum of its current value and the citation count.
    //  - Otherwise, calculate the h-index using the number of remaining papers (citations.length - i).
    if (citations[i] <= citations.length - i) {
      h_index = Math.max(h_index, citations[i]);
    } else {
      let l = citations.length - i;
      h_index = Math.max(h_index, l);
    }
  }
  // Return the maximum h_ind value:
  // - This value represents the highest h-index that satisfies the condition for the given array of citations.
  return h_index;
};

console.log("citations01", hIndex(citations01));
console.log("citations02", hIndex(citations02));
console.log("-------------------");

// ------------ SOLUTION #2 ---------------- //
// Complexity
// - Time complexity: O(n)
// - Space complexity: O(n)
// ----------------------------------------- //
const hIndex_02 = (citations) => {
  // Get the length of the citations array passed in,
  // and create a new array (+1 more index) and fill each index with 0.
  // (B/c zero indexed)
  //  - I.e. [ 0, 0, 0, 0, 0, 0 ]
  let papers = citations.length;
  let citationBuckets = new Array(papers + 1).fill(0);

  // Loop through citations (using "for of" loop)
  // Add append to "citationBuckets" array.
  //  - "Math.min" taking the smallest number between citation & papers.
  //  - then adding 1 to the result of that, at that index in the array, to 1.
  //   - E.g:
  //      [ 0, 0, 0, 1, 0, 0 ]
  //      [ 1, 0, 0, 1, 0, 0 ]
  //      [ 1, 0, 0, 1, 0, 1 ]
  //      [ 1, 1, 0, 1, 0, 1 ]
  //      [ 1, 1, 0, 1, 0, 2 ]
  for (let citation of citations) {
    citationBuckets[Math.min(citation, papers)] += 1;
  }

  // initialize empty variable
  let cumulativePapers = 0;
  // loop backwards, over length of papers (array passed in) (setting iterator equal to length of paper passed in.)
  // Loop through until cumulativePapers is greater to or equal to hIndex(index in array).
  //   - papers = 5
  //   - first iteration hIndex = 5
  for (let hIndex = papers; hIndex >= 0; hIndex--) {
    // cumulativePapers = cumulativePapers + citationBuckets[hIndex];
    //  - E.g. first iteration: cumulativePapers = cumulativePapers = 0 + 2
    //   - So cumulativePapers = 2
    //    - B/c citationBuckets[hIndex] => value in citationBuckets array at index 5 is 2.
    // Repeat until cumulativePapers is greater than or equal to hIndex
    // If so, found our hIndex, so return it.
    cumulativePapers += citationBuckets[hIndex];
    if (cumulativePapers >= hIndex) {
      return hIndex;
    }
  }
};

console.log("citations01", hIndex_02([3, 0, 6, 1, 5]));
console.log("citations02", hIndex_02([1, 3, 1]));
console.log("-------------------");

// ------------ SOLUTION #3 ---------------- //
// To compute the researcher's h-index, we can sort the citations array in non-increasing order and then iterate through the sorted array.
// - For each citation count, we compare it to the number of papers that have at least that many citations, which can be calculated as the remaining elements in the array.
// - If the citation count is greater than or equal to the number of papers with at least that many citations, we have found the h-index.
//
// Complexity
// - Time complexity: O(nlogn)
// - Space complexity:
//   - O(1), as we are sorting the array in-place and using only constant extra space.
//     - O(sort)
// ----------------------------------------- //
const hIndex_03 = (citations) => {
  const n = citations.length;
  // Given the citations array [3,0,6,1,5], we can sort it to obtain [6,5,3,1,0]
  citations.sort((a, b) => a - b);

  // Then iterate through the sorted array and for each citation count, we compare it to the number of remaining elements in the array.
  //  - For the first element, 6, there are 5 remaining elements in the array, all of which have at least 6 citations, so the h-index is 6.
  //   - For the second element, 5, there are 4 remaining elements in the array, all of which have at least 5 citations, so the h-index is 5.
  //    - For the third element, 3, there are 3 remaining elements in the array that have at least 3 citations, so the h-index is 3.
  for (let i = 0; i < n; i++) {
    // If the citation count is greater than or equal to the number of papers with at least that many citations, we have found the h-index
    if (citations[i] >= n - i) {
      return n - i;
    }
  }

  return 0;
};

console.log("citations01", hIndex_03([3, 0, 6, 1, 5]));
console.log("citations02", hIndex_03([1, 3, 1]));
console.log("-------------------");
