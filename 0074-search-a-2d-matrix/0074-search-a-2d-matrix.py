class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        search_row = -1
        
        while(top<=bottom):
            mid = top + (bottom - top)//2
            
            if target < matrix[mid][0]:
                bottom = mid-1
            else:
                search_row = mid
                top = mid+1
        
        if search_row == -1:
            return False
        
        start = 0
        end = len(matrix[0])-1
        
        while(start<=end):
            mid = start + (end - start)//2
        
            if target == matrix[search_row][mid]:
                return True
            
            if target < matrix[search_row][mid]:
                end = mid-1
            else:
                start = mid+1
            
        return False
                
        