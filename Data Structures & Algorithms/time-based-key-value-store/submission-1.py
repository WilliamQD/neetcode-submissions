from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.store:
            values = self.store[key]
            
            left = 0
            right = len(values) - 1
            res = ""

            while left <= right:
                mid = (left + right) // 2
                if timestamp == values[mid][1]:
                    return values[mid][0]
                if values[mid][1] <= timestamp:
                    left = mid + 1
                    res = values[mid][0]
                else:
                    right = mid - 1
            return res
        else:
            return ""
