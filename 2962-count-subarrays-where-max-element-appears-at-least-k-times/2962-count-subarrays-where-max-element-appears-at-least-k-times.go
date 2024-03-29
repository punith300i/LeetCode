func countSubarrays(nums []int, k int) int64 {
    var count int = 0
    var left int64 = 0
    max_element := getMaxValue(&nums)
    var ans int64 = 0
    for right:=0;right<len(nums);right++{
        if nums[right]==max_element{
            count++
        }
        for count>=k {
            if nums[left]==max_element{
                count--
            }
            left++
        }
        ans+=left
    }
    return ans
}

func getMaxValue(n *[]int) int{
    var maxVal = math.MinInt
    for _, ele := range *n{
        if ele > maxVal{
            maxVal = ele
        }
    }
    return maxVal
}