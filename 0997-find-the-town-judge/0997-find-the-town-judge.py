class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dmap1 = defaultdict(int)
        dmap2 = defaultdict(int)
        
        for a,b in trust:
            dmap1[a]+=1
            dmap2[b]+=1
            
        for i in range(1,n+1):
            if dmap2[i] == n-1 and dmap1[i] ==0:
                return i
        return -1