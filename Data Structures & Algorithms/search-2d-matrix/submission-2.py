class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        left = 0
        right = ROWS * COLS - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // COLS
            col = mid % COLS

            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        return False