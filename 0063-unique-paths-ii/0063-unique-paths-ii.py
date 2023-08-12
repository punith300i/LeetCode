class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[-1]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        return self.dfs(obstacleGrid,0,0,dp)
    def dfs(self,grid, x, y,dp):
        if(x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==1):
            return 0
        if(x == len(grid)-1 and y == len(grid[0])-1):
            return 1
        if dp[x][y] != -1: return dp[x][y]
        down = self.dfs(grid,x+1,y,dp) 
        right = self.dfs(grid,x,y+1,dp)
        result = down + right
        dp[x][y] = result
        return dp[x][y]