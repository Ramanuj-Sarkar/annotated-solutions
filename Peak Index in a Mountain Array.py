# We are given an array of at least length 3
# where the values increase to a peak and then decrease.
# We have to return the peak in O(lg(n)) time.
# We are given an array of at least length 3
# where the values increase to a peak and then decrease.
# We have to return the peak in O(lg(n)) time.
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        # it's like binary search
        while start <= end:
            # find the median
            mid = (start + end) // 2
            
            print(mid)
            
            # we know there are at least 3 values
            # so this is something we can assume is possible
            before, during, after = arr[mid - 1], arr[mid], arr[mid + 1]
            
            # O(3) so it's O(1)
            maximum = max(arr[mid - 1], arr[mid], arr[mid + 1])
            
            
            if maximum == during:  # we found the peak
                return mid
            elif maximum == before:  # the peak is to the left
                end = mid - 1
            else:  # the peak is to the right
                start = mid + 1

