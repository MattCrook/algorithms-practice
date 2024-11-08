#---------------------------------------------------------------#
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2
#---------------------------------------------------------------#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

# solution = Solution()
# print(solution.maxDepth([3,9,20,"null","null",15,7]))


class Solution_2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = []
        q.append(root)
        depth=0
        while len(q):
            dim = len(q)
            for i in range(dim):
                node=q.pop(0)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            depth+=1

        return depth

# solution_2 = Solution_2()
# print(solution_2.maxDepth([3,9,20,null,null,15,7]))


# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode() {}
#  *     TreeNode(int val) { this.val = val; }
#  *     TreeNode(int val, TreeNode left, TreeNode right) {
#  *         this.val = val;
#  *         this.left = left;
#  *         this.right = right;
#  *     }
#  * }
#  */
# class Solution {
#     public int maxDepth(TreeNode root) {
#         return maxdepth(root);
#     }
    
#     public int maxdepth(TreeNode root){
#         if(root==null){
#             return 0;
#         }
#         int lst = maxdepth(root.left);
#         int rst = maxdepth(root.right);
#         return Math.max(lst, rst)+1;
#     }
# }
