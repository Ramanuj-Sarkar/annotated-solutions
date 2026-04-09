# Find the lowest node in the tree
# which has the lowest node(s) as descendants
# (a node can be a descendant of itself)
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def lcaDFS(r: Optional[TreeNode]) -> (Optional[TreeNode], int):
            # r is None
            if not r:
                return r, 0
            
            # find children and depths
            left, left_depth = lcaDFS(r.left)
            right, right_depth = lcaDFS(r.right)

            # return one with greater depth
            # if depth is not equal
            if left_depth < right_depth:
                return right, 1 + right_depth
            elif left_depth > right_depth:
                return left, 1 + left_depth
            
            # r has greatest depth
            # so it is either the lowest node
            # or the LCA of the lowest nodes
            return r, 1 + left_depth
        
        actual_node = lcaDFS(root)[0]
        return actual_node
