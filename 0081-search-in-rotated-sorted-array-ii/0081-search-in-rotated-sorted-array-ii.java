class Solution {
    public boolean binarySearch(int nums[], int start, int end, int target){
        
        while(start<=end){
            
            int mid = start + (end-start)/2;
            
            if((nums[start] == nums[mid]) && (nums[end] == nums[mid]))
            {
                start++;
                end--;
            }

            if(nums[mid]==target){
                return true;
            }

            if(nums[mid] > target){
                end = mid - 1;
            }else{
                start = mid + 1;
            }
        }
        
        return false;
    }
    
    public boolean search(int[] nums, int target) {
        int N = nums.length;
        int start = 0;
        int end = N-1;
        int minIndex = 0;
        
        for(int i=1; i<N; i++){
            if( nums[i-1] > nums[i] ) {
                minIndex = i;
                break;
            }
        }

        
        boolean leftResult = binarySearch(nums, 0, minIndex-1, target);
        boolean rightResult = binarySearch(nums, minIndex, N-1, target);
        
        return leftResult || rightResult;
        
    }
}