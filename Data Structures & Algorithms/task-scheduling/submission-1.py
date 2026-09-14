from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        wr = deque()
        time = 0

        while max_heap or wr:
            if wr and time == wr[0][1]:
                heapq.heappush(max_heap, wr.popleft()[0])
            
            if max_heap:    
                count = heapq.heappop(max_heap)
                if count < -1:
                    wr.append([count + 1, time + n + 1])
            
            time += 1

        
        return time
