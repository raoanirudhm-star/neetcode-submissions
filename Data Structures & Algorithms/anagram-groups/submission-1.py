class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagrams = {}
        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord('a')] += 1
            if tuple(arr) not in map_anagrams:
                map_anagrams[tuple(arr)] = []
            map_anagrams[tuple(arr)].append(string)

        ans = []
        
        for groups in map_anagrams.values():
            ans.append(groups)
        
        return ans
        