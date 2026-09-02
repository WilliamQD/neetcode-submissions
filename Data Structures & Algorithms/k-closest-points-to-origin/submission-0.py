class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        points = [(-math.sqrt(x ** 2 + y ** 2), [x,y]) for x, y in points]

        heapq.heapify(points)

        while len(points) > k:
            heapq.heappop(points)
        
        return [coord for dist, coord in points]

