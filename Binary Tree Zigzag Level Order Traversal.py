# You have to return the rows of a binary tree
# but the even rows are returned read left to right
# and the odd rows are returned read right to left
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        answer, dq, left_to_right = [], deque([root]), True

        while dq:
            level = []
            for _ in range(len(dq)):
                if left_to_right:
                    node = dq.popleft()
                    level.append(node.val)

                    # right-to-left nodes
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                    print("not reverse level:", level)
                else:  # right-to-left
                    node = dq.pop()
                    level.append(node.val)

                    # left-to-right nodes
                    if node.right:
                        dq.appendleft(node.right)
                    if node.left:
                        dq.appendleft(node.left)
            answer.append(level)
            left_to_right = not left_to_right
        return answer
