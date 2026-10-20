class Solution:
    def findMin(self, nums: List[int]) -> int:
        # First we compare the median with the leftmost element
        # If the median is greater than the leftmost element but we see a smaller element on the right, we move l to m + 1
        # If the median is greater than the leftmost but we see a greater element on the right, we move r to m - 1
        # If the median is less than the leftmost element, we move r to m - 1
        l = 0
        r = len(nums) - 1
        minElem = float('inf')
        while l <= r:
            m = (l + r) // 2
            minElem = min(minElem, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return minElem


        