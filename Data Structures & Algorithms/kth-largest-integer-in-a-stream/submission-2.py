import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top = []
        self.k = k

        for num in nums:
            heapq.heappush(self.top, num)

            if len(self.top) > k:
                heapq.heappop(self.top)

    def add(self, val: int) -> int:
        heapq.heappush(self.top, val)
        if len(self.top) > self.k:
            heapq.heappop(self.top)
        return self.top[0]
