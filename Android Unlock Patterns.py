# Android unlock patterns have to be set up in a specific way
# This returns all the viable patterns consisting of at least m keys and at most n keys
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # all the numbers which have to come between two sets of numbers
        cross = {(1, 3): 2,
                 (1, 7): 4,
                 (1, 9): 5,
                 (2, 8): 5,
                 (3, 7): 5,
                 (3, 9): 6,
                 (4, 6): 5,
                 (7, 9): 8}
        
        # number of patterns
        self.patterns = 0
        
        def getValidKeys(last, seen):
            # this is the end of the range of patterns that count
            if len(seen) > n:
                return
            
            # a pattern of this length at least was seen
            elif len(seen) >= m:
                self.patterns += 1
            
            # last is included in seen
            remains = {1,2,3,4,5,6,7,8,9} - seen
            
            for number in remains:
                # fewer options if it's like this
                minnum, maxnum = min(last, number), max(last, number)
                
                # get more values if this is a valid sequence
                if not (minnum, maxnum) in cross or cross[(minnum, maxnum)] in seen:
                    getValidKeys(number, seen | {number})            
            
        for i in set(range(1,10)):
            getValidKeys(i, {i})
        
        return self.patterns
