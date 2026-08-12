from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        r = 0
        char_freq = defaultdict(int)
        
        while r < len(s):
            # 1. Add the new right character
            char_freq[s[r]] += 1
            
            most_freq = max(char_freq.values())
            numsTochange = (r - l + 1) - most_freq
            
            # 2. SHRINK LOOP: while the window is invalid, inch 'l' forward
            while numsTochange > k:
                char_freq[s[l]] -= 1
                l += 1
                
                # Must recalculate inside the loop so the while condition knows when to stop!
                most_freq = max(char_freq.values())
                numsTochange = (r - l + 1) - most_freq
            
            # 3. Update the max (we only get here when the window is 100% valid)
            longest = max(longest, r - l + 1)
            
            # 4. Move right pointer forward
            r += 1
            
        return longest