class Solution {
    public int helper(int[] nums, int target, int start, int end, String type){
        
        int res = -1;
        
        while(start <= end){
            
            int mid = start + (end - start)/2;
            
            if(nums[mid]==target){
                res = mid;
                if(type == "first"){
                    end = mid-1;
                }else{
                    start = mid+1;
                }
            }
            else if(target < nums[mid]){
                end = mid-1;
            }else{
                start = mid+1;
            }
        }
        
        return res;
        
    }
    public int[] searchRange(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        
        int[] result = new int[2];
        result[0] = helper(nums, target, start, end , "first");
        result[1] = helper(nums, target, start, end, "last");
        
        return result;
        
    }
}