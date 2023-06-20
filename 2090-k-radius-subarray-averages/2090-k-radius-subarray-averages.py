class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0 for i in range(n)]
        prefix_sum[0] = nums[0] 
        
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        result = [-1 for i in range(n)]

        for i in range(k,n-k):
            res_sum = prefix_sum[i+k]
            temp_sum = 0
            if i-k>0:
                temp_sum = prefix_sum[i-k-1]
            result[i] = (res_sum-temp_sum)//(2*k+1)
            
            
        
        return result
