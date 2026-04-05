class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # the grid doesn't exist
        if not grid:
            return 0
        
        # find the number of islands
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # set all contiguous parts of the island to seen / water
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        
        if (r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] == "0"):
            
            return
        
        # set it to seen
        grid[r][c] = "0"

        # set the ones around it to seen
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
        
