from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = defaultdict(int)

        for t in tasks:
            freq[t] += 1
        
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        wr = deque()

        time = 0
        while max_heap or wr:
            if wr and time == wr[0][1]:
                task = wr.popleft()
                count = task[0]
                heapq.heappush(max_heap, count)
            
            if max_heap:    
                count = heapq.heappop(max_heap)
            else:
                count = 0 

            time += 1

            if count < -1:
                wr.append([count + 1, time + n])

        
        return time
