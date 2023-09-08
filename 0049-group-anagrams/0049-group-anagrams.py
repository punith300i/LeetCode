class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(str_val)) for str_val in strs]
        smaps = {}
        result = []
        for i,j in zip(sorted_strs,strs):
            if i not in smaps:
                smaps[i] = [j]
            else:
                smaps[i].append(j)
        for i,j in smaps.items():
            result.append(j)
        return result