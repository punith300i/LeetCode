class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dirs = [-1,0,1]
        
        dp_memo = {}
        
        def rec_func(row, r1, r2):
            if row == len(grid) or r1<0 or r1>=len(grid[0]) or r2<0 or r2>=len(grid[0]):
                return 0
            
            # memoization
            if (row,r1,r2) in dp_memo:
                return dp_memo[(row,r1,r2)]
            
            cherries = 0
            if r1!=r2:
                cherries = grid[row][r1] + grid[row][r2]
            else:
                cherries = grid[row][r1]
            
            max_val = 0
            for dr1 in dirs:
                for dr2 in dirs:
                    max_val = max(max_val, rec_func(row+1, r1 + dr1, r2 + dr2))
            
            dp_memo[(row,r1,r2)] = cherries + max_val
            
            return dp_memo[(row,r1,r2)]
    
        return rec_func(0,0,len(grid[0])-1)
        
                        