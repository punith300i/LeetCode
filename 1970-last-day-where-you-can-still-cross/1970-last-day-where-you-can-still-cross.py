class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def bfs(day):
            grid = [[0 for _ in range(col)] for _ in range(row)]
            
            queue = deque()
            visited = set()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for r,c in cells[:day]:
                grid[r-1][c-1] = 1
            
            for c in range(col):
                if not grid[0][c]:
                    queue.append((0,c))
                    visited.add((0,c))
            
            while queue:
                
                r,c = queue.popleft()
                
                if r == row-1:
                    return True
                
                for nx,ny in directions:
                    x = r+nx
                    y = c+ny
                    
                    if x in range(row) and y in range(col) and grid[x][y]==0 and (x,y) not in visited:
                        queue.append((x,y))
                        visited.add((x,y))
                        
            
            return False
        
        l = 0
        r = len(cells)-1
        result = 0
        
        while l<=r:
            mid = l + (r-l)//2
            
            if bfs(mid):
                result = mid
                l = mid+1
            else:
                r = mid-1
        
        return result