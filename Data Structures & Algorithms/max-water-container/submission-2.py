class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxWater = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            area = min(heights[left], heights[right]) * (right - left) 
            maxWater = max(maxWater, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater