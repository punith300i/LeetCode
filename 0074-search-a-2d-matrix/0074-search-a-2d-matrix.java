class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int top = 0;
        int bottom = matrix.length-1;
        int row = -1;
        
        while(top<=bottom){
            int mid = top + (bottom-top)/2;
            if(matrix[mid][0] > target){
                bottom = mid-1;
            }else{
                row = mid;
                top = mid+1;
            }
        }
        
        if(row==-1){
            return false;
        }
        
        int start = 0;
        int end = matrix[0].length -1;
        
        while(start<=end){
            int mid = start + (end-start)/2;
            
            if(matrix[row][mid]==target){
                return true;
            }
            
            if(matrix[row][mid] > target){
                end = mid-1;
            }else{
                start = mid+1;
            }
        }
        
        return false;
    }
}