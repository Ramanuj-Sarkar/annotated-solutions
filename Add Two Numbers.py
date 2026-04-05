class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m1, m2 = l1, l2  # go through loop
        prel3 = m3 = ListNode()  # answer
        carry = 0

        while m1 or m2 or carry:
            carry, rem = divmod((m1.val if m1 else 0) +
                                (m2.val if m2 else 0) +
                                carry, 10)
            m3.next = m3 = ListNode(rem)
            m1 = m1.next if m1 else None
            m2 = m2.next if m2 else None
        
        return prel3.next
