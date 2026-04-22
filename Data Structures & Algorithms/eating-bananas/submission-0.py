import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)

        while min_k < max_k:
            mid = (min_k + max_k) // 2

            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / mid)
            
            if hours_spent > h:
                min_k = mid + 1
            else:
                max_k = mid
        
        return max_k