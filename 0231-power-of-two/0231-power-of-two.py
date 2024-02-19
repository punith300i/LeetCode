class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        memo = {}
        def dp(n):
            if n==1:
                return True  
            if n%2==1 or n==0:
                return False  
            
            # memo
            if n in memo:
                return memo[n]
            
            memo[n] = dp(n//2)
            return memo[n]
        
        return dp(n)