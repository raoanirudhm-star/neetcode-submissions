class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        # []
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] + nums[k] == target:
                        j += 1            
                elif nums[j] + nums[k] < target:
                    j += 1               
                else:
                    k -= 1
        return ans
                

        