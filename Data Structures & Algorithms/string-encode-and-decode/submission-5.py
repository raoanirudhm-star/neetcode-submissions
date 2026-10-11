class Solution:

    def encode(self, strs: List[str]) -> str:
        # We need to encode length and then have a delimiter
        cypher = ""
        for word in strs:
            cypher += str(len(word)) + '#' + word
        return cypher

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            n = int(s[i:j])
            i = j + 1
            ans.append(s[i:i+n])
            i += n
        return ans

