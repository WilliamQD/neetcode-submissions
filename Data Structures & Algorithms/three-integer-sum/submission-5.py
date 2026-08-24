class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue 
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
                    