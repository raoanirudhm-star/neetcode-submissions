class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while num in num_set:
                    length += 1
                    num += 1
                ans = max(ans, length)
        return ans