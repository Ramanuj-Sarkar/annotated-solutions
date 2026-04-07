# nodes which help implement the class
class MinNode:
    def __init__(self, val=None):
        self.val = val
        self.prev = self.next = None

# this is like a normal stack
# but you have to get the minimum in O(1) time
# this is sure to be O(1) unlike the canonical solution
class MinStack:

    def __init__(self):
        # a pointer to the top of the minimum value
        # but not the actual minimum value
        self.min_head = MinNode()
        
        # a pointer to the top value
        # but not the actual one
        self.head = MinNode()
        

    def push(self, val: int) -> None:
        
        # works even if old_top is None
        old_top = self.head.next
        self.head.next = MinNode(val)
        self.head.next.next = old_top
        
        if not self.min_head.next:
            # just add the value
            # because it's the only value
            # so it's the minimum
            self.min_head.next = MinNode(val)
        else:
            # you have an old value
            old_min = self.min_head.next
            min_val = old_min.val

            # you need to make sure it's the minimum
            if val < min_val:
                self.min_head.next = MinNode(val)
            else:
                self.min_head.next = MinNode(min_val)
            self.min_head.next.next = old_min
        

    def pop(self) -> None:
        # just get the next value
        # it won't be empty
        new_top = self.head.next.next
        new_min = self.min_head.next.next

        self.head.next = new_top
        self.min_head.next = new_min

    def top(self) -> int:
        return self.head.next.val
        

    def getMin(self) -> int:
        return self.min_head.next.val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
