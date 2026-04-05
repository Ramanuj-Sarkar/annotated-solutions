# comments should explain everything
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        subs = ''
        
        for x in s:
            if x not in subs: # this isn't a repeat
                subs += x
                n = max(len(subs), n) # save the longest length of these 
            else: # get rid of the repeat from before
                subs = subs[subs.index(x)+1:] + x # this can, at most, be the exact same length
        
        return n
