import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for i in range(n)]
        res = []
        
        def queen_check(row_index, col_index, board):
            row = row_index
            col = col_index
            # left
            while row>=0 and col>=0:
                if board[row][col] == "Q":
                    return False
                col-=1    
            
            row = row_index
            col = col_index
            # up-left
            while row>=0 and col>=0:
                if board[row][col] == "Q":
                    return False
                row-=1
                col-=1
                        
            row = row_index
            col = col_index
            # down-left
            while row<n and col>=0:
                if board[row][col] == "Q":
                    return False
                row+=1
                col-=1
            
            return True

        def rec_func(col_index, board):
            nonlocal res
            
            if col_index == n:
                res.append(copy.deepcopy(board))
                return

            for row_index in range(n):
                if queen_check(row_index, col_index, board):
                    board[row_index][col_index] = "Q"
                    rec_func(col_index+1, board)
                    board[row_index][col_index] = '.'
        
        rec_func(0,board)
        
        for i in range(len(res)):
            res[i] = list(map(lambda x: ''.join(x), res[i]))
            
        return res
            
        
        