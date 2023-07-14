class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 1
        
        for i in range(len(arr)):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i]-difference] + 1
            else:
                dp[arr[i]] = 1
        
            res = max(res, dp[arr[i]])
        
        return res