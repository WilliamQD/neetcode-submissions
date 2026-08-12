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

        # insane opt
        left = 0
        right = len(nums) - 1
        
        # 1. Use < instead of <=
        while left < right:
            mid = (left + right) // 2
            
            # 2. Only compare against the RIGHT pointer
            if nums[mid] > nums[right]:
                # The "cliff" is to the right. 
                # Since mid is strictly greater than right, mid CANNOT be the minimum.
                left = mid + 1 
            else:
                # We are past the cliff, or there is no cliff.
                # The minimum is at mid or to the left of it.
                right = mid
                
        # 3. When the loop breaks, left == right, which is pointing directly at the minimum
        return nums[left]