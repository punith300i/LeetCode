class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        rows = len(s)+1
        cols = len(t)+1
        dp = [[0 for i in range(cols)] for i in range(rows)]
        
        for i in range(rows):
            dp[i][cols-1] = 1
        
        for i in range(len(s))[::-1]:
            for j in range(len(t))[::-1]:
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] += dp[i+1][j]
                    
        return dp[0][0]
        