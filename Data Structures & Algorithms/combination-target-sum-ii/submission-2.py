class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(j, path, total):
            # exit conditions
            if total == target:
                result.append(path[:])
                return

            if total > target or j >= len(candidates):
                return

          
            path.append(candidates[j])
            backtrack(j+1, path, total+candidates[j])
            path.pop()

            while j + 1 < len(candidates) and candidates[j] == candidates[j+1]:
                j += 1
            backtrack(j+1, path, total)


            
        backtrack(0, [], 0)
        return result