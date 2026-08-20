class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def backtrack(j, path, total):
            if total == target:
                result.append(path[:])
                return

            if total > target or j >= len(nums):
                return


            path.append(nums[j])            
            backtrack(j, path, total + nums[j])
            path.pop()
            backtrack(j+1, path, total)


            # add current item to path, j unchanged (keep adding)  
            # add current item to path, increase j
            # dont add current, increase j




    
        
        result = []
        backtrack(0, [], 0)
        return result