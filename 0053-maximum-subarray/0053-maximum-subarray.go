func maxSubArray(nums []int) int {
    curSum := 0
    maxSum := -math.MaxInt-1
    
    for _, elem := range nums{
        curSum += elem
        maxSum = max(maxSum, curSum)
        if curSum < 0{
            curSum = 0
        }
    }
    
    return maxSum
}