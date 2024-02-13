class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        prefix_sum = [nums[0]]
        res = 0
        
        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        for i in range(len(nums)):
            if prefix_sum[i]-k in hmap:
                res += hmap[prefix_sum[i]-k]
            
            hmap[prefix_sum[i]] = hmap.get(prefix_sum[i],0) + 1
        
        return res