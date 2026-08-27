from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    queue.append((i,j))

        sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            i, j = queue.popleft()

            for di, dj in sides:
                if 0 <= di + i < r and 0 <= dj + j < c and grid[di+i][dj+j] == 2147483647:
                    grid[di+i][dj+j] = grid[i][j] + 1

                    queue.append((di+i, dj+j))
                    
        