class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        
        rows,cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def bfs(sx,sy):
            vis = set()
            queue.append((sx,sy))
            vis.add((sx,sy))

            while queue:
                x,y = queue.popleft()
                
                if board[x][y] == "O":
                    board[x][y] = "T"
                    
                for dx,dy in directions:
                    adj_x = x+dx
                    adj_y = y+dy
                    if adj_x in range(0,rows) and adj_y in range(0,cols) and(adj_x,adj_y) not in vis:
                            if board[adj_x][adj_y]=="O":
                                queue.append((adj_x, adj_y))
                                vis.add((adj_x, adj_y)) 
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0,rows-1] or c in [0,cols-1]):
                    bfs(r,c)
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
                    