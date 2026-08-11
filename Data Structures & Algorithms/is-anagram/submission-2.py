from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for i in range(len(s)):
            map1[s[i]] += 1
            map2[t[i]] += 1

        return map1 == map2