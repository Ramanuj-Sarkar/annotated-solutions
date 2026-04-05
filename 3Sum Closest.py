# find the three numbers in nums which sum to the target value
# or find the three numbers which come closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minsum = nums[0] + nums[1] + nums[2]  # smallest sum

        sortnums = sorted(nums)  # sorting lets you make assumptions about changes

        for x in range(len(sortnums)):  # sortnums[x] is the smallest
            left = x + 1
            right = len(sortnums) - 1
            while left < right:
                
                newsum = sortnums[x] + sortnums[left] + sortnums[right]
                
                if newsum == target:
                    return newsum
                elif abs(target - newsum) < abs(target - minsum):
                    minsum = newsum
                
                if newsum < target:
                    left += 1
                else:
                    right -= 1
        return minsum
