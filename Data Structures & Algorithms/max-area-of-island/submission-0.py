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
            
            sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            area = 1
            
            for dr, dc in sides:
                area += dfs(r + dr, c + dc)
            
            return area

        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea