# serialize(tree) turns the tree into a string
# deserialize(string) turns the string into a tree 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        
        def recur(root):
            """
            recursive helper function which checks all nodes of root
            """
            if root is None:  # check base case
                return "None"
            else:  # single string call
                return f"{root.val},{recur(root.left)},{recur(root.right)}"
        
        return recur(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')

        def iterate(n: int):
            """
            recursive helper function that iterates over list
            """
            if data_list[n] == 'None':
                return None, n + 1
                
            root = TreeNode(data_list[n])
            n += 1
            root.left, n = iterate(n)
            root.right, n = iterate(n)
            return root, n

        return iterate(0)[0]


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
