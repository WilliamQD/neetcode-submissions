
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = [0] * 26
        for s in s1:
            s1_list[ord(s) - ord('a')] += 1

        l = 0
        s2_list = [0] * 26
        
        for r in range(len(s2)):

            if (r - l + 1) > len(s1):
                s2_list[ord(s2[l]) - ord('a')] -= 1
                l += 1
            s2_list[ord(s2[r]) - ord('a')] += 1
            
            if s1_list == s2_list:
                return True

        return False
            

            
                
