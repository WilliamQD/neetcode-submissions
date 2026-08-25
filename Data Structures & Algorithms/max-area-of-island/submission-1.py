class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        h = len(grid)
        w = len(grid[0])

        def dfs(r, c):
            # 1. Base Case: If out of bounds or water, this contributes 0 area.
            if r < 0 or r >= h or c < 0 or c >= w or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            
            return 1 + dfs(r - 1, c) + \
                       dfs(r + 1, c) + \
                       dfs(r, c - 1) + \
                       dfs(r, c + 1)

        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea