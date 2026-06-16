class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        track_letters = [0]*26

        for i in range(len(s)):
            track_letters[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            idx = ord(t[i]) - ord('a')
            if track_letters[idx] < 1:
                return False
            else:
               track_letters[idx] -= 1 
        
        return track_letters == [0] * 26


        