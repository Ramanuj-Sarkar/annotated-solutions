# We have a grid where '0' is water and '1' is land.
# For each piece of land, cells connected horizontally and vertically are part of the same piece of land
# while cells connected diagonally are not.
# We have to find the number of connected series of 1.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0

        # store all visited cells
        visited = set()

        # m = rows, n = columns
        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                curr = (x, y)
                if curr not in visited and grid[x][y] == '1':
                    # add it to the islands
                    answer += 1

                    # queue for BFS
                    positions = []
                    positions.append(curr)

                    while positions:
                        this_x, this_y = positions[0]

                        # add positions to visited
                        visited.add(positions[0])

                        # you're just checking the corresponding cell
                        # and adding it if it's 1 and hasn't been visited yet
                        if this_x > 0:
                            up = (this_x - 1, this_y)
                            if up not in visited and grid[up[0]][up[1]] == '1':
                                visited.add(up)
                                positions.append(up)
                        if this_x < m - 1:
                            down = (this_x + 1, this_y)
                            if down not in visited and grid[down[0]][down[1]] == '1':
                                visited.add(down)
                                positions.append(down)                            
                        if this_y > 0:
                            left = (this_x, this_y - 1)
                            if left not in visited and grid[left[0]][left[1]] == '1':
                                visited.add(left)
                                positions.append(left)                            
                        if this_y < n - 1:
                            right = (this_x, this_y + 1)
                            if right not in visited and grid[right[0]][right[1]] == '1':
                                visited.add(right)
                                positions.append(right)

                        # queue behavior
                        positions = positions[1:]

        return answer
        
