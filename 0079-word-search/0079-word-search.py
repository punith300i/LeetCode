class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0,-1],[1,0],[0,1],[-1,0]]
        visited = set()
        
        def traverse(index, row, col):            
            if index == len(word):
                return True
            
            if row not in range(len(board)) or col not in range(len(board[0])) or board[row][col]!=word[index] or (row,col) in visited:
                return False
            
            visited.add((row,col))
            
            for x,y in dirs:
                ncol = col+y
                nrow = row+x
                if traverse(index+1, nrow, ncol) :
                    return True
            
            visited.remove((row,col))
            
            return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if traverse(0,i,j):
                        return True
        return False
                    
            
            