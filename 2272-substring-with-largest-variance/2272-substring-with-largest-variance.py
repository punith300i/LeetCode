class Solution:
    def largestVariance(self, s: str) -> int:
        freq = {}
        res = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0) + 1
        for a,b in itertools.permutations(freq,2):
            max_val=0
            has_a,has_b = False,False
            remain_a,remain_b = freq[a],freq[b]
            for ch in s:
                if ch!=a and ch!=b:
                    continue
                if max_val<0 and remain_a!=0 and remain_b!=0:
                    max_val=0
                    has_a,has_b = False,False
                if ch==a: 
                    max_val+=1
                    remain_a-=1
                    has_a = True
                elif ch==b:
                    max_val-=1
                    remain_b-=1
                    has_b = True
                if has_a and has_b:
                    res = max(res, max_val)
        return res