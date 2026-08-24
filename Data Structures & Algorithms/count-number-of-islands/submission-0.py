class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        h = len(grid)
        w = len(grid[0])

        def backtrack(i, j):
            if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            island = True
            for di, dj in sides:
                backtrack(i + di, j + dj)
                    
        for a in range(h):
            for b in range(w):
                if grid[a][b] == '1':
                    count += 1
                    backtrack(a, b) 
        return count