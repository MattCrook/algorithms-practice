#--------------------------------------------------------#
# Convert Sorted Array to Binary Search Tree
#
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#--------------------------------------------------------#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Recursion
# Since nums is a sorted list, the middle element nums[len(nums)//2] must be the root node of nums.
#Thus, after setting the middle element be the root, finding the middle element in the left subarry nums[:len(nums)//2] and right subarry nums[len(nums)//2 + 1 : ]
class Solution_1(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )


solution_1 = Solution_1()
print(solution_1.sortedArrayToBST([-10,-3,0,5,9]))
print(solution_1.sortedArrayToBST([1,3]))
print("--------------------------")




# Solution 2
class Solution_2(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(arr, s, e):
            if s > e:
                return None
            mid = s + (e - s) // 2
            node = TreeNode(arr[mid])
            node.left = helper(arr, s, mid - 1)
            node.right = helper(arr, mid + 1, e)
            return node

        n = len(nums)
        if n == 0:
            return None
        return helper(nums, 0, n - 1)

solution_2 = Solution_2()
print(solution_2.sortedArrayToBST([-10,-3,0,5,9]))
print(solution_2.sortedArrayToBST([1,3]))
print("--------------------------")



# Solution 3
class Solution_3:
    def sortedArrayToBST(self, nums):
        n = len(nums)

        if not n:
            return None

        mid = (n-1)//2
        root = TreeNode(nums[mid])

        root.left = (self.sortedArrayToBST(nums[:mid]))
        root.right = (self.sortedArrayToBST(nums[mid+1:]))

        return root

solution_3 = Solution_3()
print(solution_3.sortedArrayToBST([-10,-3,0,5,9]))
print(solution_3.sortedArrayToBST([1,3]))
print("--------------------------")
