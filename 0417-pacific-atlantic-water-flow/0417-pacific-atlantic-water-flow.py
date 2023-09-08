class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(i, j, visit, prev_height):
            if i<0 or j<0 or i>=rows or j>=cols or heights[i][j] < prev_height or (i,j) in visit:
                return
            visit.add((i,j))
            dfs(i+1,j,visit, heights[i][j])
            dfs(i-1,j,visit, heights[i][j])
            dfs(i,j+1,visit, heights[i][j])
            dfs(i,j-1,visit, heights[i][j])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        result = []
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
        
        return result
            