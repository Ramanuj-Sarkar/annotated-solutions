# Comments explain even simple things.
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dici = {}  # all the i fruits
        start = 0  # first tree you take fruits from
        ans = 0  # how many trees
        
        for end, val in enumerate(fruits):
            dici[val] = dici.get(val, 0) + 1
            
            # this means a new value has been added
            # or the old one isn't there
            # it can't be an if-statement because you can't skip trees
            # you have to stop taking fruits from ALL the trees before you start
            while len(dici) > 2:
                start_val = fruits[start]  # start tree
                dici[start_val] -= 1
                if not dici[start_val]:  # no more of that tree
                    dici.pop(start_val)
                start += 1  # should you not have taken the fruit of the i+1th tree?
            ans = max(ans,end - start + 1)  # is this the longest?
        
        return ans
