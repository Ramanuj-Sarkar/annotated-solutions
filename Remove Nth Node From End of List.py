# You need to remove the Nth from the end.
# For example, if n is 2, you remove the second-to-last node.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast finds the end
        # slow finds the nth from the end
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        # this means we have to remove head
        # we just return head.next
        if not fast:
            return head.next
        # now fast is finding the end
        while fast.next:
            fast, slow = fast.next, slow.next
        # now it skips the nth node from the end
        slow.next = slow.next.next
        return head
        
