class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        
        key_count = 0
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == '@':
                    start = [i,j]
                if grid[i][j] in 'abcdef':
                    key_count+=1
                
        
        q = collections.deque()
        q.append((start[0],start[1],''))
        
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        result_steps = 0
        
        while q:
            
            for _ in range(len(q)):
                r,c,keys = q.popleft()

                if (r,c,keys) in visited: continue

                if len(keys) == key_count:
                    return result_steps

                visited.add((r,c,keys))

                for nx, ny in directions:
                    x = r+nx
                    y = c+ny

                    if x in range(nrows) and y in range(ncols) and grid[x][y]!='#':

                        if grid[x][y] in '.@':
                            q.append((x,y,keys))

                        if grid[x][y] in 'abcdef' and grid[x][y] not in keys:
                            q.append((x,y,keys+grid[x][y]))

                        if grid[x][y] in 'abcdef' and grid[x][y] in keys:
                            q.append((x,y,keys))

                        if grid[x][y] in 'ABCDEF' and grid[x][y].lower() in keys:
                            q.append((x,y,keys))

            result_steps+=1
            
        return -1