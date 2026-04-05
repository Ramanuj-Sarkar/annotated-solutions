# Merge k sorted linked lists.
# Return None if there are no lists.
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        if not lists:  # no lists
            return None
        
        l1 = lists.pop()
        
        while lists:  # while there are more lists
            l2 = lists.pop()  # take this list out
            l1 = self.merge_lists(l1, l2)  # merge it with the old one
        
        return l1
    
    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node  # lets you return the head
        
        while l1 and l2:
            if l1.val > l2.val:  # add the node in l2 if it's smaller
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1  # add the node in l1 otherwise
                l1 = l1.next
            node = node.next

        # add the remaining nodes to the new linked list
        if l1:
            node.next = l1
        else:
            node.next = l2
        
        return ans.next
        
