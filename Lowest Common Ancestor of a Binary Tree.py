# Find the lowest node in the tree
# which has both p and q as descendants
# (a node can be a descendant of itself).
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # either the root is None (returns None)
        # or the root is p / q (returns that)
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if we are in this situation
        # both left and right have returned a node
        # so it branches here
        if left and right:
            return root
        
        # if left is None, return right
        # you only check if right is None if left is None
        return left if left else right
        
