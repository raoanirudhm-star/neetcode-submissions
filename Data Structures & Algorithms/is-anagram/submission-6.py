class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_mapping_s = {}
        letter_mapping_t = {}
        for i in range(len(s)):
            if s[i] in letter_mapping_s:
                letter_mapping_s[s[i]] += 1
            else:
                letter_mapping_s[s[i]] = 1
            if t[i] in letter_mapping_t:
                letter_mapping_t[t[i]] += 1
            else:
                letter_mapping_t[t[i]] = 1
        return letter_mapping_s == letter_mapping_t
        
        