'''
The integer side represents the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

The 2D integer array points has the coordinates of points lying on the boundary of the square.

The Manhattan Distance between two cells (x, y) and (j, k) is |x - j| + |y - k|.

Select k elements among points such that the minimum Manhattan distance between any two points is maximized.

Return the maximum possible minimum Manhattan distance between the selected k points.
'''
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        res = []

        # Classify the points into categories based on positions
        # relative to the square's four sides.
        for x, y in points:
            if x == 0:
                res.append(y)
            elif y == side:
                res.append(side + x)
            elif x == side:
                res.append(side * 3 - y)
            else:
                res.append(side * 4 - x)
        
        # Sort the points in a clockwise direction
        # for easier traversal and calculation of distances.
        res.sort()

        # checks if it's possible to achieve k valid moves
        # with a given distance n
        # by comparing the distance between points 
        # and checking if we can make enough moves to satisfy the condition
        # it essentially checks if mid should be the new ceiling (False) or floor (True)
        def low_enough(n : int) -> bool:
            idx = [0] * k
            curr = res[0]
            for i in range(1, k):
                j = bisect_left(res, curr + n)
                # j == len(res) means it takes
                # an impossible number of moves
                # so we should look lower
                if j == len(res):
                    return False
                idx[i] = j
                curr = res[j]
            # even the final res[j] isn't that high
            # so we should look higher
            if curr - res[0] <= side * 4 - n:
                return True
            
            for idx[0] in range(1, idx[1]):
                for j in range(1, k):
                    while res[idx[j]] < res[idx[j - 1]] + n:
                        idx[j] += 1
                        # it takes an impossible number of moves
                        # we should look lower
                        if idx[j] == len(res):
                            return False
                
                # even the final res[idx[-1]] isn't that high
                # so we should look higher
                if res[idx[-1]] - res[idx[0]] <= side * 4 - n:
                    return True
            
            # we should look lower
            return False
        
        # binary search to find the largest possible distance
        # that allows at least k valid moves
        left, right = 1, side + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if low_enough(mid):
                left = mid
            else:
                right = mid
        
        # return the minimum
        return left
