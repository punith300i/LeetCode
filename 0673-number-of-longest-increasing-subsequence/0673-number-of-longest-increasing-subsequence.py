class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        counts = [1] * len(nums)
        res = 0
        
        max_val = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        counts[i] = counts[j]
                    elif dp[i] == dp[j]+1:
                        counts[i]+=counts[j]
                
                max_val = max(max_val, dp[i])
        
        for i in range(len(nums)):
            if dp[i]==max_val:
                res+=counts[i]
                
        return res