class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d= collections.Counter(arr)
        return len(d.values())==len(set(d.values()))