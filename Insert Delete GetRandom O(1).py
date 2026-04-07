# implements a data structure which can
# insert, delete, and get a random element
# in constant time
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """

        # the dict allows for constant-time delete / checking
        self.dict = {}

        # the list allows for constant-time getrandom
        self.list = []

        
    def insert(self, val: int) -> bool:
        """
        Returns true if the set did not already contain the specified element.
        Returns false otherwise.
        Inserts a value to the set if it wasn't already there.
        """
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        
        return True
        

    def remove(self, val: int) -> bool:
        """
        Returns true if the set contained the specified element.
        Removes the value if it was there.
        Otherwise return false 
        """
        if val in self.dict:
            # swap the last element and the one that's being deleted
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            
            # delete the (new) last element
            # pop() is O(1) but pop(index) is O(N)
            self.list.pop()
            del self.dict[val]
            
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
