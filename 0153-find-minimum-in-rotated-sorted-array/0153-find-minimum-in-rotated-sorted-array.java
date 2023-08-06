class Solution {
    public int findMin(int[] nums) {
        int N = nums.length;
        int start = 0;
        int end = N - 1;
        
        while(start<=end){
            int mid = start + (end-start)/2;
            
            int next = (mid + 1)%N;
            int prev = (mid + N -1)%N;
            
            if (nums[mid] <= nums[next] && nums[mid] <= nums[prev]){
                return nums[mid];
            }
            
            if(nums[0] <= nums[mid]){
                start = mid+1;
            }else if (nums[end] >= nums[mid]){
                end = mid-1;
            }
        }
        
        return nums[0];
        
    }
}