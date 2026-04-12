'''
You are given an m x n binary matrix grid.

In one operation, choose any row or column and flip each value in it
(i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if you can all 1's from the grid
or false otherwise.

You can use any number of operations.
'''

# You can only do horizontal / vertical flips
# so you either change all rows at once
# or invert all cells in one column for all
 
# This means all of the rows have to be 
# either the same or an inversion of each other.

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # All of the rows have to be either the same
        # or an inversion of each other.
        normal, inverted = grid[0], [1-val for val in grid[0]]

        for i in range(1, len(grid)):
            if grid[i] not in (normal, inverted):
                return False
        
        return True
