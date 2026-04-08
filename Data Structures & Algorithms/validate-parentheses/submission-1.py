class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for brac in s:
            if brac in closeToOpen:
                if stack and stack[-1] == closeToOpen[brac]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brac)
        
        if stack:
            return False
        return True