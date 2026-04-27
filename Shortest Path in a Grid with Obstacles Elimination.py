'''
There is an m x n integer matrix where each cell is either 0 (empty) or 1 (obstacle).

You start in the upper left corner (0,0)
and can move up, down, left, or right to an adjacent cell.

Return the minimum number of steps
to walk from the upper left corner (0, 0)
to the lower right corner (m - 1, n - 1)
given that you can eliminate at most k obstacles.

If it is not possible to find such a walk, return -1.
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        target = (m - 1, n - 1)

        # if we have sufficient quotas to eliminate the obstacles in the worst case,
        # then the shortest distance is the Manhattan distance
        if k >= m + n - 2:
            return m + n - 2

        # (row, col, remaining quota to eliminate obstacles)
        state = (0, 0, k)
        
        # queue to find answer and conduct BFS
        queue = deque([(0, state)])

        # which ones were seen
        seen = {state}

        while queue:
            steps, (row, col, k2) = queue.popleft()

            # we reach the target here
            if (row, col) == target:
                return steps

            new_steps = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]

            # explore the four directions in the next step
            for new_row, new_col in new_steps:
                # if (new_row, new_col) is within the grid boundaries
                if (0 <= new_row < m) and (0 <= new_col < n):
                    new_eliminations = k2 - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)
                    
                    # add the next move in the queue if it qualifies
                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))

        # did not reach the target
        return -1
