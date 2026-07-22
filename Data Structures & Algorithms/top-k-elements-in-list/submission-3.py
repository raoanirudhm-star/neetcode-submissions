class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_freq = {}
        for num in nums:
            map_freq[num] = 1 + map_freq.get(num, 0)
        freq_arr = [[] for i in range(len(nums) + 1)]
        for num, freq in map_freq.items():
            freq_arr[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []


        