class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n_stones = [-x for x in stones]
        heapq.heapify(n_stones)

        while len(n_stones) > 1:

            stone1 = -heapq.heappop(n_stones)
            stone2 = -heapq.heappop(n_stones)

            remain = abs(stone1 - stone2)
            if remain:
                heapq.heappush(n_stones, -remain)
        
        if len(n_stones) == 0:
            return 0
        return -n_stones[0]

        
            
