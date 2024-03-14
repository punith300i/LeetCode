int helper(int *nums, int goal, int n){
    if(goal<0){
        return 0;
    }
    
    int l = 0;
    int res = 0;
    int cur_val = 0;
    for(int r=0; r<n; r++){
        cur_val = cur_val + nums[r];
        while(cur_val > goal){
            cur_val = cur_val - nums[l];
            l = l + 1;
        }
        res = res+(r-l+1);
    }
    return res;
}

int numSubarraysWithSum(int* nums, int numsSize, int goal){
    
    return helper(nums, goal, numsSize) - helper(nums,goal-1, numsSize);
}