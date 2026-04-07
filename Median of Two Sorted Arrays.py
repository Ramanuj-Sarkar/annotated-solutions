# imagine the two sorted arrays were merged
# without actually merging them, find what the median would be
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 must be smaller
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        # the low and high values show what the median has to be between
        # they start on either side of the smaller array for that reason
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # partX is the middle index of low and high
            partX = (low + high) // 2
            partY = (x + y + 1) // 2 - partX
            
            # this stars as the maximum value of the left half of the smaller array
            # and the minimum value of the right half of that array
            # and eventually becomes these values with regards to the whole thing
            maxlX = float('-inf') if partX == 0 else nums1[partX - 1]
            minrX = float('inf') if partX == x else nums1[partX]
            
            # this is the same thing for the larger array
            maxlY = float('-inf') if partY == 0 else nums2[partY - 1]
            minrY = float('inf') if partY == y else nums2[partY]
            
            print(maxlX, minrX, "vs", maxlY, minrY)

            if maxlX <= minrY and maxlY <= minrX:
                # the left and right halves of both arrays correspond
                # the values keep moving such that the median is
                # eventually in the left arrays if it's odd

                if (x + y) % 2 == 0:  # even type of median (between two values)
                    return (max(maxlX, maxlY) + min(minrX, minrY)) / 2.0
                else:  # odd type of median (single value)
                    return float(max(maxlX, maxlY))
            elif maxlX > minrY:
                # the median has to be to the left
                print("left")
                high = partX - 1
            else:
                # the median has to be to the right
                print("right")
                low = partX + 1
                
        return 0.0
