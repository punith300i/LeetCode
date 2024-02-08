class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for j in range(i):
                if i-j*j<0:
                    break
                dp[i]=min(dp[i],1+dp[i-j*j])

        return dp[n]