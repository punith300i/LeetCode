class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashmap = {0:1}
        prefix_sum = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        
        res = 0
        for i in range(len(nums)):
            if prefix_sum[i] - k in hashmap:
                res = res + hashmap[prefix_sum[i]-k]
            
            hashmap[prefix_sum[i]] = hashmap.get(prefix_sum[i],0) + 1
        
        return res