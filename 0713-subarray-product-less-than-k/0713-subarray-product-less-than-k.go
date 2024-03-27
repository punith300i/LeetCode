func numSubarrayProductLessThanK(nums []int, k int) int {
    var product int=1
    var left,count int = 0, 0
    
    if k<=1{
        return 0
    }
    
    for right:=0; right<len(nums);right++{
        product *= nums[right]
        for product>=k{
            product = product/nums[left]
            left++
        }
        count += right-left+1
    }
    return count
}