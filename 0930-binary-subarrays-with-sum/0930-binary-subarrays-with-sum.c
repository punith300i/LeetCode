func helper(nums []int, x int) int {
    
    if x<0 {
        return 0
    }
    
    var l int = 0
    var res int = 0
    var current_val int = 0
    for r, ele := range nums{
        current_val = current_val + ele
        for current_val > x {
            current_val = current_val - nums[l]
            l = l + 1
        }
        res = res + r-l + 1
    }
    return res
}

func numSubarraysWithSum(nums []int, goal int) int {
    return helper(nums, goal) - helper(nums, goal-1)
}