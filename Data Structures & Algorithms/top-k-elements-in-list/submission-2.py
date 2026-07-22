class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_freq = {}
        for num in nums:
            map_freq[num] = 1 + map_freq.get(num, 0)
        
        min_heap = []
        for num in map_freq.keys():
            heapq.heappush(min_heap, (map_freq[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        while len(min_heap) > 0:
            res.append(min_heap[0][1])
            heapq.heappop(min_heap)
        
        return res

        