from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        fresh = 0
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        if not queue:
            return -1
        
        sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()
            state = grid[i][j]

            for di, dj in sides:
                nr, nc = i + di, j + dj
                if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 1:
                    # print(f"found row {i} col {j}, change to {grid[i][j] + 1}")
                    grid[nr][nc] = state + 1
                    queue.append((nr, nc))
        
        max_minute = -1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
                max_minute = max(max_minute, grid[i][j])
        return max_minute - 2