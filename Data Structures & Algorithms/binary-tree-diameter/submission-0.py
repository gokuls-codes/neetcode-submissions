# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return 0, 0
            
            lHeight, lMax = helper(node.left)
            rHeight, rMax = helper(node.right)

            return max(lHeight, rHeight) + 1, max(lMax, rMax, lHeight + rHeight)

        return helper(root)[1]