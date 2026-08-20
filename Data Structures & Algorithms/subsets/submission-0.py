class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(j, path):

            if j >= len(nums):
                result.append(path[:])
                return
            
            path.append(nums[j])
            backtrack(j + 1, path)
            path.pop()

            backtrack(j+1, path)








        
        result = []
        backtrack(0, [])
        return result