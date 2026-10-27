class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        l, r = -1, m - 1
        ans = 0
        while l <= r:
            cut_nums1 = (l + r) // 2
            cut_nums2 = (m + n - 1) // 2 - cut_nums1 - 1
            left1 = nums1[cut_nums1] if cut_nums1 >= 0 else float('-inf')
            right1 = nums1[cut_nums1+1] if cut_nums1 + 1 < m else float('inf')
            left2 = nums2[cut_nums2] if cut_nums2 >= 0 else float('-inf')
            right2 = nums2[cut_nums2+1] if cut_nums2 + 1 < n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                   return max(left1, left2)
            elif left1 > right2:
                r = cut_nums1 - 1
            else:
                l = cut_nums1 + 1
        return ans





        