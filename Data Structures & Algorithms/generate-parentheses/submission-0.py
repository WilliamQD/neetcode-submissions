class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(path, left, right):
            if left == right == n:
                result.append("".join(path))
                return

            if left > n or right > n:
                return 

            # left
            path.append("(")
            backtrack(path, left + 1, right)
            path.pop()
            
            # right
            if right < left:
                path.append(")")
                backtrack(path, left, right + 1)
                path.pop()
        
        backtrack([], 0, 0)
        return result

        # []
        #   [(]
        #       [((]
        #           [(((]
        #               [((((]
        #               [((()]