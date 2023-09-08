class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
                return 0
            grid[i][j]="#"
            c=1
            c+=dfs(grid,i+1,j)
            c+=dfs(grid,i-1,j)
            c+=dfs(grid,i,j+1)
            c+=dfs(grid,i,j-1)
            
            return c
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, dfs(grid,i,j))
        
        return max_area