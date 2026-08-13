class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3, 4, 5, 6, 1, 2] left and right both smaller, mid larger , go left
        # [3, 4, 0, 1, 2] left and right both smaller, mid smaller, go left
        # [6, 1, 2, 3, 4, 5] mid smaller, left and right both larger, go right
        # [8, 1, 5, 6, 7] mid larger, left and right both larger, go left; this is wrong huh
        # [2, 3/5, 7] left smaller right larger, mid small go right mid large go left
        # [7, 8/1, 2] left larger right smaller, mid small impossible mid large also impossible

        # go right when  mid smaller, left and right both larger or left smaller right larger, mid small go right mid


        left = 0
        right = len(nums) - 1

        while left <=  right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]:
                # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1        
        return -1

        # mid = 2, 