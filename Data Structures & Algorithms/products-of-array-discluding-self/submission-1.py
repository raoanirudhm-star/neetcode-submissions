class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 2, 4, 6
        # Prefixes: [1, 1, 2, 8]
        # Suffixes: [48, 24, 6, 1]
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] * nums[i + 1]

        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefixes[i] * suffixes[i]
        return ans

        