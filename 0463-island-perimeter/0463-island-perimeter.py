class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [[0,-1],[1,0],[0,1],[-1,0]]
        visited=set()
        
        def traverse(row, col):
            
            if row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col]!=1:
                return 1
            
            if (row,col) in visited:
                return 0
            
            visited.add((row,col))
            
            res = 0
            for x,y in dirs:
                nrow = row+x
                ncol = col+y
                res+=traverse(nrow,ncol)
            
            return res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return traverse(i,j)