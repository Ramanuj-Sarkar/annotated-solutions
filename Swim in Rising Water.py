'''
You are given an n x n integer matrix grid
where each value represents the elevation at that point.

Water gradually rises over time. At time t, the water level is t.

You can swim from a square to another 4-directionally adjacent square
if and only if the elevation of both squares individually are at most t.

You can swim infinite distances in zero time.
You must stay within the boundaries of the grid during your swim.
Each of the values in the grid is unique.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1)
if you start at the top left square (0, 0).

'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # both sides are n long
        n = len(grid)

        # values within edges contain:
        # time - the value of that node
        # u - the cell's placement in i.e. an array
        # v - if i > 0, the cell above / if j > 0, the cell to the left
        edges = []

        for i in range(n):
            for j in range(n):
                if i > 0:
                    edges.append((max(grid[i][j], grid[i-1][j]), i*n+j, (i-1)*n+j))
                if j > 0:
                    edges.append((max(grid[i][j], grid[i][j-1]), i*n+j, i*n+j-1))
        
        # cells are sorted based on weights
        edges.sort()

        parent = list(range(n * n))
        
        # query existing sets
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # merge two sets together
        def union(x, y):
            parent[find(x)] = find(y)
        
        # keep joining sets
        # then try to find whether 0 and n*n-1 are connected
        for time, u, v in edges:
            union(u, v)
            if find(0) == find(n*n-1):
                return time
        
        # if there is only one element
        return grid[0][0]
