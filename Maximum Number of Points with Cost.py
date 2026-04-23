'''
You have an m x n integer matrix points (0-indexed).
You want to maximize the number of points you can get from the matrix.

Picking the cell at coordinates (r, c) will add the value of that cell to your score.

For every two adjacent cells,
picking cells at coordinates (r, c1) and (r + 1, c2)
will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # rows of maximum points
        curr_row = [0] * len(points[0])
        prev_row = [0] * len(points[0])
        
        for row in points:
            # eventually contains the maximum at this point
            run_max = 0

            # find the value the cells in row would propagate if they were all 0
            # subtracting from run_max due to distance condition
            # and finding the maximum value
            for j in range(len(row)):
                run_max = max(run_max - 1, prev_row[j])
                curr_row[j] = run_max
            
            # find the value the cells have in practice
            # when added to the relevant maximum value
            for j in range(len(row)-1,-1,-1):
                run_max = max(run_max - 1, prev_row[j])
                curr_row[j] = max(curr_row[j], run_max) + row[j]
            
            # switch the row names to show the next row is here
            prev_row = curr_row

        # because prev_row is what curr_row used to be
        return max(prev_row)
