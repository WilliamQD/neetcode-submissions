class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive method, with sorting
        # freq = Counter(nums).most_common(k)
        # return [item[0] for item in freq]

        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in freq:
            bucket[freq[num]].append(num)
        
        result = []
        while len(result) < k:
            if bucket[-1] == []:
                bucket.pop()
            else:
                result.append(bucket[-1].pop())
        return result


