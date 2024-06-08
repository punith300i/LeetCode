func checkSubarraySum(nums []int, k int) bool {
    remMap := map[int]int{0:-1}
    rem := 0
    for i, _ := range nums{
        rem = (rem + nums[i])%k
        if _, ok := remMap[rem]; ok {
            if i - remMap[rem] > 1{
                return true
            }
        }else{
            remMap[rem]=i
        }
    }
    return false
}