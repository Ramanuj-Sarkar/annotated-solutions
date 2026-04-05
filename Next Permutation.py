# comments should explain everything
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # find first decreasing element from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # if i == -1, you reverse the whole thing
        if i > -1:
            j = n - 1
            # find just larger element
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse the suffix / whole thing
        nums[i + 1:] = reversed(nums[i + 1:])
