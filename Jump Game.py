# The array shows the maximum jump forward you can make from that point
# You start at the first element of the array
# Return true if you can reach the end by jumping forward and false if you can't.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumping = 0
        for n in nums:
            if jumping < 0: # you can't jump this far
                return False
            elif n > jumping: # you would jump to this location
                jumping = n
            
            jumping -= 1 # you try jumping to the next one
            
        return True
