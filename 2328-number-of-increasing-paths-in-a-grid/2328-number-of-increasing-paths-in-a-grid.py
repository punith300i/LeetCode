class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9+7
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        result = 0
        
        @cache
        def dfs(i,j):
            
            res = 1
            
            for dx,dy in directions:
                if (0 <= i+dx < m) and (0 <= j+dy < n) and (grid[i+dx][j+dy] > grid[i][j]):
                    res += dfs(i+dx,j+dy)
        
            return res
        
        for i in range(m):
            for j in range(n):
                result = (result+ (dfs(i,j)%mod))%mod
        
        return result