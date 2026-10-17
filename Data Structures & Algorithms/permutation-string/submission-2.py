class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1FreqMap = [0] * 26
        currFreqMap = [0] * 26

        for i in range(len(s1)):
            s1FreqMap[ord(s1[i]) - ord('a')] += 1
            currFreqMap[ord(s2[i]) - ord('a')] += 1
        
        if s1FreqMap == currFreqMap:
            return True
        
        for i in range(len(s1), len(s2)):
            currFreqMap[ord(s2[i]) - ord('a')] += 1
            currFreqMap[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if s1FreqMap == currFreqMap:
                return True
        return False

