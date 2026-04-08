class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = min(heights[start], heights[end]) * end

        while start < end:
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            curr_area = min(heights[start], heights[end]) * (end - start)
            max_area = max(max_area, curr_area)

        return max_area

                