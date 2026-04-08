class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])
        
        postfix = [1] * len(nums) 
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        return [p * s for p, s in zip(prefix, postfix)]