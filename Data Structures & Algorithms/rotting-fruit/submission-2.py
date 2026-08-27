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
        minutes = 0
        
        while queue and fresh > 0:
            minutes += 1

            for _ in range(len(queue)):
                i, j = queue.popleft()

                for di, dj in sides:
                    nr, nc = i + di, j + dj
                    if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
        
        return minutes if fresh == 0 else -1