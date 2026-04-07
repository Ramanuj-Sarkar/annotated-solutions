# You have a sorted list and a target int
# You have to find the first and last instances of that int
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower, upper = self.lowerBound(nums, target), self.upperBound(nums, target)

        return [lower, upper]
    
    def lowerBound(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2

            if nums[mid] >= target:
                # We find the first instance
                # if the beginning of the array is the target
                # or the value before mid is less than the target
                if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                    return mid
                
                # Search on the left side
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1
    
    def upperBound(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2

            if nums[mid] <= target:
                # We find the last instance
                # if the end of the subarray is the target
                # or the value after mid is more than the target
                if nums[mid] == target and (mid == end or nums[mid + 1] > target):
                    return mid
                
                # Search on the left side
                begin = mid + 1
            else:
                end = mid - 1
        
        return -1
        
