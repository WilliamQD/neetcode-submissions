class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n_stones = [-x for x in stones]
        heapq.heapify(n_stones)

        while len(n_stones) > 1:

            stone1 = heapq.heappop(n_stones)
            stone2 = heapq.heappop(n_stones)

            if stone1 != stone2:
                # s1 is more negative, so s1 - s2 keeps the result negative!
                heapq.heappush(n_stones, stone1 - stone2)
        
        return -n_stones[0] if n_stones else 0

        
            
