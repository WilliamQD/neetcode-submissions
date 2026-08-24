class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)

        if n == 0:
            return []


        digToL = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        def letters(path, idx):

            if len(path) == n:
                return result.append("".join(path))

            digit = digits[idx]
            
            for c in digToL[digit]:
                path.append(c)
                letters(path, idx + 1)
                path.pop()
                
        letters([], 0)
        return result

            

        
