class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in seen_chars:
                while s[l] != s[r]:
                    seen_chars.remove(s[l])
                    l += 1
                l += 1
            else:
                seen_chars.add(s[r])
                ans = max(ans, r - l + 1)
        return ans
        