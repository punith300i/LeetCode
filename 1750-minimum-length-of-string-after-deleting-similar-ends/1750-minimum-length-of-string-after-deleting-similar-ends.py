class Solution:
    def minimumLength(self, s: str) -> int:
        lprev, l = 0, 0
        rprev, r = len(s)-1, len(s)-1
        
        while l<r:
            if s[l] == s[r]:
                l+=1
                while l<r and s[l-1]==s[l]:
                    l+=1
                r-=1
                while l<r and s[r+1]==s[r]:
                    r-=1
            else:
                break
                
        return r-l+1
            
                    