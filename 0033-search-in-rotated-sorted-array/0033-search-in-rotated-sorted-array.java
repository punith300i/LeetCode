class Solution {
    
    public int binarySearch(int[] nums, int start, int end, int target){
        while(start<=end){
            int mid = start + (end-start)/2;

            if(nums[mid]==target){
                return mid;
            }
            
            if(nums[mid] < target){
                start = mid+1;
            }else{
                end = mid-1;
            }
        }
        return -1;
    }
    
    public int search(int[] nums, int target) {
        int N = nums.length;
        int start = 0;
        int end = N - 1;
        int result = -1;
        
        int minIndex = 0;
        
        while(start<=end){
            int mid = start + (end-start)/2;
            
            int next = (mid + 1)%N;
            int prev = (mid + N -1)%N;
            
            if (nums[mid] <= nums[next] && nums[mid] <= nums[prev]){
                minIndex = mid;
            }
            
            if(nums[0] <= nums[mid]){
                start = mid+1;
            }else if (nums[end] >= nums[mid]){
                end = mid-1;
            }
        }

        result = binarySearch(nums, 0, minIndex-1, target);

        if(result!=-1){
            return result;
        }
        
        result = binarySearch(nums, minIndex, N-1, target);
        
        if(result!=-1){
            return result;
        }
        
        return result;
        
    }
}