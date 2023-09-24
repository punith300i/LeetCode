class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        c = Counter()
        res = 0
        for r in range(len(s)):
            c[s[r]]+=1
            if r-l+1 - c.most_common(1)[0][1] <= k:
                res = r-l+1
            else:
                c[s[l]]-=1
                l+=1
                
        return res