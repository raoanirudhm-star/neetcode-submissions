class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in memory:
                return [min(memory[diff], i), max(memory[diff], i)]
            else:
                memory[nums[i]] = i
        return []
        