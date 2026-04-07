# Find the subarray of nums with the largest sum. Return that sum.
# The subtle O(n) way is self.byOn
# the suble O(lgn) way is self.byDivide
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subtle = False
        
        if subtle:
            return self.byDivide(nums)
        else:
            return self.byOn(nums)
    
    def byOn(self, nums: List[int]) -> int:
        max_sum = start_sum = - math.inf
        
        for end in nums:  # imagine the end 
            start_sum = max(start_sum + end, end)
            max_sum = max(max_sum, start_sum)
        
        return max_sum
        

    def byDivide(self, nums: List[int]) -> int:
    
        def recurrer(left: int, right: int) -> int:
            # empty array
            if left > right:
                return - math.inf
        
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(curr, best_left_sum)
            
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(curr, best_right_sum)
            
            best_combined_sum = best_left_sum + nums[mid] + best_right_sum

            left_half, right_half = recurrer(left, mid - 1), recurrer(mid + 1, right)

            return max(left_half, best_combined_sum, right_half)
        
        return recurrer(0, len(nums) - 1)
