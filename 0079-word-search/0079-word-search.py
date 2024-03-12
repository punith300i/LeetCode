class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0,-1],[1,0],[0,1],[-1,0]]
        visited = set()
        
        def traverse(index, row, col):            
            if index == len(word):
                return True
            
            for x,y in dirs:
                if 0<=row+x<len(board) and 0<=col+y<len(board[0]) and board[row+x][col+y] == word[index]:
                    ncol = col+y
                    nrow = row+x
                    if (nrow,ncol) not in visited:
                        visited.add((nrow,ncol))
                        if traverse(index+1, nrow, ncol) :
                            return True
                        else:
                            visited.remove((nrow,ncol))
            return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if traverse(1,i,j):
                        return True
                    else:
                        visited.remove((i,j))
        return False
                    
            
            