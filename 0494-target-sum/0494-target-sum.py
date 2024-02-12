class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[-1 for i in range(sum(nums)*2 + 1)] for i in range(len(nums))]
        def rec_func(index,s):
            
            if index < 0 and s == target:
                    return 1
                
            if index < 0:
                    return 0
            
            if dp[index][s]!=-1:
                return dp[index][s]
            
            
            pos = rec_func(index-1, s + nums[index])
            neg = rec_func(index-1, s + (-1 * nums[index]))
            
            dp[index][s] = pos+neg
            
            return dp[index][s]
        
        return rec_func(len(nums)-1,0)