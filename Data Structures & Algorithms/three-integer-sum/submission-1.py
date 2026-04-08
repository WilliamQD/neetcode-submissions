class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip if this is the same 'fixed' value
            # we can just check one before bcuz its sorted

            if i > 0 and a == nums[i-1]:
                continue

            # now perform 2sums
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res