# Some of the numbers in nums have smaller numbers to the right.
# Return an array result where for each nums[i]
# result[i] is the number of smaller elements to the right.
class Solution:
    def mergeCount(self, nums: List[List[int]], start: int, end: int, result: List[int]):
        if start >= end:
            return

        mid = (start + end) // 2

        left_pos, right_pos = start, mid + 1

        self.mergeCount(nums, left_pos, mid, result)
        self.mergeCount(nums, right_pos, end, result)

        merged = []

        right_lt_left = 0

        while left_pos < mid + 1 and right_pos <= end:

            if nums[left_pos][1] > nums[right_pos][1]:
                # we know the number on the right is smaller
                # than the number of the left
                # and the left subarray is already sorted
                # so nums[right_pos] must be smaller than everything else there
                right_lt_left += 1

                # this is just merge sort stuff
                merged.append(nums[right_pos])
                right_pos += 1
            else:
                # the number from the left
                # is not greater than the one from the right
                # so the index is moved
                result[nums[left_pos][0]] += right_lt_left

                # merge sort
                merged.append(nums[left_pos])
                left_pos += 1
        
        # merge sort moves all remaining into merged result
        while left_pos < mid + 1:
            result[nums[left_pos][0]] += right_lt_left
            merged.append(nums[left_pos])
            left_pos += 1
        
        while right_pos <= end:
            merged.append(nums[right_pos])
            right_pos += 1
        
        # copying merged result into array
        # for merge sort
        pos = start
        for m in merged:
            nums[pos] = m
            pos += 1


    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        result = [0] * n

        ordered_nums = [[i, num] for i, num in enumerate(nums)]
        
        # doing merge sort gives the answer for this
        # and sorts the array as a byproduct
        self.mergeCount(ordered_nums, 0, n - 1, result)

        return [r for r in result]
