class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while left <= right: 
            if right - left == 1:
                return nums[right] if nums[right] < nums[left] else nums[left]

            mid = (left + right) // 2

            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        
        return -1