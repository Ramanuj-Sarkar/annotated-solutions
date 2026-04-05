"""
Makes a deep copy of a linked list 
where each node has a next pointer pointing to the next value
and a random pointer pointing to another value
both of these have to stay the same in the copy
(like, if next = 1 and random = 5 in the original, it's also like that in the deep copy)
it returns a pointer to the head

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # no head means no new list
        if not head:
            return None
        
        # the dictionary has the values of the nodes
        old_to_new = {}
        
        # create nodes with the values in each node
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # set the next and random pointers for each new node
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        
        return old_to_new[head]
  
