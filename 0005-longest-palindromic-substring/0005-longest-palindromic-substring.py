class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_len = float('-inf')
        result = None
        for i in range(len(s)):
            
            # odd
            l = i
            r = i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if r-l+1 > cur_len: 
                    cur_len = max(cur_len, r-l+1)
                    result = s[l:r+1]
                l-=1
                r+=1
            
            # even
            l = i
            r = i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if r-l+1 > cur_len: 
                    cur_len = max(cur_len, r-l+1)
                    result = s[l:r+1]
                l-=1
                r+=1
        
        return result