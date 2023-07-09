class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 1
    
        cur = pairs[0][1]
        for p in pairs[1:]:
            if cur<p[0]:
                res+=1
                cur=p[1]
        
        return res