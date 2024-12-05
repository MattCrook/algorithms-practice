//--------------------------------------------------------//
// Convert Sorted Array to Binary Search Tree
//
// Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.//
// Example 1:
// Input: nums = [-10,-3,0,5,9]
// Output: [0,-3,9,-10,null,5]
// Explanation: [0,-10,5,null,-3,null,9] is also accepted:
//
// Example 2:
// Input: nums = [1,3]
// Output: [3,1]
// Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
//--------------------------------------------------------//



// -------------------//
/*
TreeNode class:
- Defines the structure for each node in the tree, with properties val, left, and right representing the node's value and its left and right children, respectively.

sortedArrayToBST function:
- Takes a sorted array nums as input.
- It uses a helper function buildBST(left, right) to recursively construct the binary search tree.
- The mid index of the current subarray is chosen as the root of the subtree.
- Recursively builds the left subtree using the left half of the array and the right subtree using the right half.
- Recursive Helper Function: The buildBST function is used to divide the array into subarrays and recursively build the tree:

If the left index is greater than the right index, it means there are no elements left to form a subtree, so it returns null.
- Otherwise, it creates a node with the middle value and proceeds to construct the left and right subtrees.

Example Output:
- For the input array[-10, -3, 0, 5, 9], the output will be a balanced binary search tree. (Here’s a textual representation):
        0
       / \
     -3   5
     /     \
   -10      9
*/
// -------------------//


// Definition for a binary tree node.
class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function sortedArrayToBST(nums) {
  // Helper function to build the BST recursively
  function buildBST(left, right) {
    if (left > right) {
      return null; // Base case: no elements to form a subtree
    }

    // Find the middle element to be the root of the current subtree
    const mid = Math.floor((left + right) / 2);
    const node = new TreeNode(nums[mid]);

    // Recursively build the left and right subtrees
    node.left = buildBST(left, mid - 1);
    node.right = buildBST(mid + 1, right);

    return node;
  }

  return buildBST(0, nums.length - 1);
}

// console.log(arrayToBinarySearchTree([-10, -3, 0, 5, 9]));
// console.log(arrayToBinarySearchTree([1, 3]));
// console.log("--------------------------");
const bstRoot = sortedArrayToBST([-10, -3, 0, 5, 9]);
console.log(bstRoot);
console.log("-------");
const bstRoot2 = sortedArrayToBST([1, 3]);
console.log(bstRoot2);
console.log("-------------------------------");




// function arrayToBinarySearchTree(numbers, left = 0, right = numbers.length - 1) {
//   if (left > right) {
//     return null;
//   }
// }


// console.log(arrayToBinarySearchTree([-10, -3, 0, 5, 9]));
// console.log(arrayToBinarySearchTree([1, 3]));
// console.log("--------------------------");
