class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        ans = 0
        majority = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            if freq[s[r]] > majority:
                majority = freq[s[r]]
            # We check whether we have exceeded the maximum number of replacements. We also check if the current letter exceeds the majority count.
            while (r - l + 1) - majority > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        
        return ans
            





        
        
        