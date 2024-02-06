class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sorted_strings = list(enumerate([(''.join(sorted(string))) for string in strs]))
        hashmap = defaultdict(list)
        for idx, string in sorted_strings:
            hashmap[string].append(strs[idx])
        return hashmap.values()
        