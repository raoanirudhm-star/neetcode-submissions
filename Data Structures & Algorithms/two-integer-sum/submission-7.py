class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_indices = {}
        for i in range(len(nums)):
            lookup = target - nums[i]
            if lookup in map_indices:
                return [map_indices[lookup], i]
            else:
                map_indices[nums[i]] = i
        return []
        