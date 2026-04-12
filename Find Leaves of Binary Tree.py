'''
You have the root of a binary tree.
You have to return a list of lists of ints.
You put all of the values of the leaf nodes into the 0th list.
You put all of the nodes with a height of 1 into the first list.
You put all of the nodes with a height of 2 into the second list, etc.

They have to be ordered from left to right.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.findLevel(root, levels)
        return levels

    def findLevel(self, root: Optional[TreeNode], val_list) -> int:
        if not root:
            return -1
        
        left = self.findLevel(root.left, val_list)
        right = self.findLevel(root.right, val_list)
        
        level = max(left, right) + 1

        if level == len(val_list):
            val_list.append([])
        
        val_list[level].append(root.val)

        return level
