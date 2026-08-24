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
        def letters(path_str, idx):

            if idx == n:
                result.append(path_str)
                return
            
            for c in digToL[digits[idx]]:
                letters(path_str + c, idx + 1)
                
        letters("", 0)
        return result

            

        
