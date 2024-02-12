class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        for i in nums:
            hmap[i]+=1
        max_val = max(hmap.values())
        for i in hmap.keys():
            if hmap[i] == max_val:
                return i
        return 0