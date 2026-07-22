class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            get_len = ""
            while s[i] != '#':
                get_len += s[i]
                i += 1
            length = int(get_len)
            i += 1
            word = s[i:i+length]
            res.append(word)
            i += length
        return res  
