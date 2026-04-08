class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char.lower() for char in s if char.isalnum())

        midway = len(clean_s) // 2

        for i in range(midway):
            if clean_s[i] != clean_s[-i - 1]:
                return False
        return True