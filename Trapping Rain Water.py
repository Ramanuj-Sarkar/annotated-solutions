# You have a list of 2D spike heights, essentially
# and you have to figure out how much water is in between them.
# It's kind of like:
# [2, 0, 1, 1, 1, 2, 0, 0, 1]
# corresponds to
# X     X
# X XX XX  X
# and you figure out how much water would get stuck here (w is water)
# XwwwwwX
# XwXXwXXwwX
class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        leftMax = 0
        rightMax = 0
        totalWater = 0

        while start < end:

            leftMax = max(leftMax, height[start]) 
            rightMax = max(rightMax, height[end])
            
            # leftMax and rightMax now have to be
            # at least equal to these heights

            if leftMax < rightMax:  # find whichever height is smaller
                totalWater += leftMax - height[start]  # this is 0 or more
                start += 1
            else:
                totalWater += rightMax - height[end]  # this is also 0 or more
                end -= 1
                
            # in both cases, the water is at least 0
            # and increases when there's something to the left or right

        return totalWater
