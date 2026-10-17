class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        First we have a frequency mapping of t
        We then increase the window iterating over s only adding relevant characters:
            - We only add characters in the set of t including duplicates. If adding a character goes over the  limit, we don't add it. For example a 3rd a when we only have 2 in the set of t
        When our tracking set reaches t's set, we then minimize the window with a left pointer until we no longer match again, tracking length here and changing our answer is a new smaller string is available
        """

        freqMapT = {}
        freqMapCurr = {}
        lenAns = float('inf')
        start = 0
        l = 0
        have = 0
        need = len(set(t))

        for i in t:
            freqMapT[i] = 1 + freqMapT.get(i, 0)

        for r in range(len(s)):
            freqMapCurr[s[r]] = 1 + freqMapCurr.get(s[r], 0)
            if s[r] in freqMapT and freqMapCurr[s[r]] == freqMapT[s[r]]:
                have += 1

            while (have == need):
                if lenAns > r - l + 1:
                    lenAns = r - l + 1
                    start = l
                
                freqMapCurr[s[l]] -= 1
                if s[l] in freqMapT and freqMapCurr[s[l]] < freqMapT[s[l]]:
                    have -= 1
                l += 1

        return "" if lenAns == float('inf') else s[start:start+lenAns]
                

            

        



        