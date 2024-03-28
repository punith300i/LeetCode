func maxSubarrayLength(nums []int, k int) int {
    var hmap = map[int]int{}
    var left int= 0
    var max_length int = math.MinInt64
    
    for right:=0;right<len(nums);right++{
        if _, ok := hmap[nums[right]];ok{
            hmap[nums[right]]++
            
            for hmap[nums[right]] > k {
                hmap[nums[left]]--
                left++
            }
            
        }else{
            hmap[nums[right]]=1
        }
        max_length = MaxValue(max_length, right-left+1)
    }
    return max_length
}

func MaxValue(i,j int) int {
    if i<j{
        return j
    }else{
        return i
    }
}