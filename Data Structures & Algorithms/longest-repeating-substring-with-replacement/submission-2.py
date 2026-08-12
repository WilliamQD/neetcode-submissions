from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        l = 0
        r = 1

        char_freq = defaultdict(int)
        char_freq[s[0]] = 1

        while r < len(s):
            char_freq[s[r]] += 1 #x=1, y=1 | x=1,y=2 | x=2,y=2
            most_freq = max(char_freq.values()) # 1, 2, 2
            numsTochange = (r - l) - most_freq + 1 # 1, 1, 2
            if numsTochange <= k:
                longest = max(longest, numsTochange + most_freq) # 2, 3, 4
            else:
                char_freq[s[l]] -= 1  # Remove the character we are leaving behind
                l += 1                # Inch the window forward

            r += 1 # 2, 3
        
        return longest