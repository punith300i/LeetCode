class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        max_val = max(hmap.values())
        return sum([v for k,v in hmap.items() if v == max_val])