impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut zeros = 0i32;
        let mut ones_zero_prod = 1i32;
        let mut total_prod = 1i32;
        
        for i in 0..nums.len(){
            if nums[i]==0{
                zeros = zeros+1;
            }else{
                ones_zero_prod = ones_zero_prod * nums[i];
            }
            total_prod = total_prod * nums[i];
        }
        
        let mut ans = vec![0; nums.len()];
        for i in 0..nums.len(){
            if zeros>1{
                ans[i] = 0;
                continue
            }else if nums[i]==0{
                ans[i] = ones_zero_prod;
            }else{
                ans[i] = total_prod/nums[i];
            }
        }
        
        return ans;
    }
}