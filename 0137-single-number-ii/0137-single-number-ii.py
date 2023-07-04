class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = Counter()
        
        for i in nums:
            count_map[i]+=1
        
        for k,v in count_map.items():
            if v!=3:
                return k
        return 0