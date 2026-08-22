class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        nums_len = len(nums)
        result = []

        def backtrack(path):
            if len(path) == nums_len:
                result.append(path[:])
                return
            


            for n in nums:
                if n in path:
                    continue

                path.append(n)
                backtrack(path)
                path.pop()
                
        backtrack([])
        return result
        
        # [], b(1, [1])
        # [1], b(2, [1, 2])
        # [1, 2], b(3, [1, 2, 3])
        # appends [1, 2, 3], pop twice, j was 2
        # [1], b(2, [1])