# Split nums into k non-empty subarrays
# such that the largest sum of any subarray is minimized
# and return that largest sum.
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def min_subarrays(sum_ceiling: int) -> int:
            curr_sum = splits_num = 0

            for num in nums:
                if curr_sum + num <= sum_ceiling:
                    # sum doesn't exceed ceiling
                    curr_sum += num
                else: # sum exceeds ceiling
                    curr_sum = num
                    splits_num += 1
            
            # number of subarrays is number of splits + 1
            return 1 + splits_num

        # left and right boundaries of binary search
        # largest subarray sum must be at least max if k == len(nums)
        # and at most sum if k == 1
        left, right = max(nums), sum(nums)
        
        # this is the worst-case sum
        smallest = right

        while left <= right:
            # this is the new attempt at a smallest sum
            curr_sum_ceiling = (left + right) // 2

            if min_subarrays(curr_sum_ceiling) <= k:
                # if required splits <= k
                # this is the new sum
                # we move to the left
                right = curr_sum_ceiling - 1
                smallest = curr_sum_ceiling
            else:
                # too many splits
                # we need to look at larger sums
                left = curr_sum_ceiling + 1
        
        return smallest
