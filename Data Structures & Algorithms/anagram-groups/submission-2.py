class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            mapping = [0] * 26
            for char in word:
                mapping[ord(char) - ord('a')] += 1
            key = tuple(mapping)
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)
        ans = []
        for value in anagram_map.values():
            ans.append(value)
        return ans

                

            
        