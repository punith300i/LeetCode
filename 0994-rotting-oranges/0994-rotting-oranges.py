class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        
        
        def bfs(two_list):
            vis = set()
            queue = deque()
            max_mins = 0
            
            for node in two_list:
                queue.append((node[0],node[1],max_mins))
                vis.add((node[0],node[1]))
            
            while queue:
                
                x,y,cur_mins = queue.popleft()

                if grid[x][y]==1:
                    grid[x][y]=3
                
                for dx,dy in directions:
                    
                    adj_x = x + dx
                    adj_y = y + dy
                    
                    if adj_x in range(0,rows) and adj_y in range(0,cols) and (adj_x,adj_y) not in vis:
                        if grid[adj_x][adj_y] == 1:
                            queue.append((adj_x,adj_y,cur_mins+1))
                            max_mins = max(max_mins, cur_mins+1)
                            vis.add((adj_x,adj_y))
            return cur_mins
        
        result = 0
        
        two_list = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    two_list.append((r,c))
        if two_list:          
            result = bfs(two_list)
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return result