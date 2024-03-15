func productExceptSelf(nums []int) []int {
    var zeros_count int = 0
    var one_zero_prod int = 1
    var total_prod int = 1

    for _, ele := range nums{
        if ele==0{
            zeros_count = zeros_count+1
        }else{
            one_zero_prod = one_zero_prod * ele
        }
        total_prod = total_prod * ele
    }
    
    for i, _ := range nums{
        if zeros_count > 1{
            nums[i] = 0
            continue
        }else if nums[i] == 0{
            nums[i] = one_zero_prod
        }else{
            nums[i] = total_prod/nums[i]
        }
    }
    
    return nums
}