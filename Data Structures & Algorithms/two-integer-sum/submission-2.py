class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in val:
                return [val[diff], i]
            
            val[num] = i