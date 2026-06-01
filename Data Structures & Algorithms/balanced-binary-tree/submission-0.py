# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return 0, True
            
            rHeight, rIsBalanced = helper(node.right)
            lHeight, lIsBalanced = helper(node.left)

            if not rIsBalanced or not lIsBalanced:
                return 0, False
            
            return max(rHeight, lHeight)+1, abs(rHeight-lHeight) <= 1
        
        return helper(root)[1]