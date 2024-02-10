class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        
        def dfs(s):
            
            if s not in res:
                res.add(s)
            
            for i in range(len(tiles)):
                if not freq[i]:
                    freq[i]=1
                    dfs(s+tiles[i])
                    freq[i]=0
        
        freq = [0] * len(tiles)
        dfs("")
        return len(res)-1
        