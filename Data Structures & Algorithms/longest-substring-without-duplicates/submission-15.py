class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in index_map:
                l = max(l, index_map[s[r]] + 1)
            index_map[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans
        