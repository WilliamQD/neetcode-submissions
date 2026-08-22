class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        def backtrack(j, path):
            if j >= len(nums):
                result.append(path[:])
                return

            # include branch
            path.append(nums[j])
            backtrack(j+1, path)
            path.pop()

            # skip branch
            while j+1 < len(nums) and nums[j] == nums[j+1]:
                j+=1
            backtrack(j+1, path)

        backtrack(0, [])
        return result

        # [1]
        #     [1, 1]
        #         [1, 1, 2], append
        #         [1, 1], append
        #     [1]
        #         [1, 2], append
        #         [1], append
        
        # [1]
        #     [1, 2], append
        #     [1], append
        # [2]
        # []
