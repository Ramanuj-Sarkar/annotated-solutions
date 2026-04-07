# node that makes implementation easier
class LRUNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


# Implement a  Least Recently Used (LRU) cache.
class LRUCache:

    '''
    Initializes LRU cache with positive capacity
    '''
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("expected 'capacity' to have value from 1 to 3000 only")
        self.capacity = capacity
        self.dic = {}

        self.head = LRUNode(-1, -1)
        self.tail = LRUNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    '''
    Return the value of the key if the key exists.
    Otherwise, return -1.
    '''
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]

        # Refresh node's usage
        self.remove(node)
        self.add(node)

        return node.val
        
    '''
    Update the value of the key if the key exists.
    Otherwise, add the key-value pair to the cache.
    If the number of keys exceeds the capacity from this operation,
    evict the least recently used key.
    '''
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        
        node = LRUNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            oldest = self.head.next
            self.remove(oldest)
            del self.dic[oldest.key]
    
    '''
    Adds node to LRUNode pointers.
    '''
    def add(self, node: LRUNode) -> None:
        second_newest = self.tail.prev
        second_newest.next = node
        node.prev = second_newest
        node.next = self.tail
        self.tail.prev = node
    
    '''
    Remove node from LRUNode pointers.
    '''
    def remove(self, node: LRUNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
