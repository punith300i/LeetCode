class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[-1 for i in range(len(t))] for i in range(len(s))]
        
        def rec_func(s_index: int, t_index: int) -> int:
            
            if t_index >= len(t):
                return 1
            if s_index >= len(s):
                return 0
            
            if dp[s_index][t_index]!=-1:
                return dp[s_index][t_index]
            
            res = 0
            if s[s_index] == t[t_index]:
                res += rec_func(s_index+1, t_index+1) + rec_func(s_index+1, t_index)
            else:
                res += rec_func(s_index+1, t_index)
            dp[s_index][t_index] = res
            
            return dp[s_index][t_index]
        
        return rec_func(0,0)