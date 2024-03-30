func subarraysWithKDistinct(nums []int, k int) int {
    // to get exactly K, we can subtract at most k value with the at most k-1 value
    return atMostK(&nums, k) - atMostK(&nums,k-1)
}

func atMostK(n *[]int, k int) int{
    var hmap = map[int]int{}
    left, count, res := 0, 0, 0
    for right:=0; right<len(*n); right++{
        // if n[right] is not visited
        if hmap[(*n)[right]] == 0{
            count++
        }
        hmap[(*n)[right]]++
        for count > k{
            hmap[(*n)[left]]--
            // if nums[left] is removed and only one if it is present
            if hmap[(*n)[left]] == 0{
                count--
            }
            left++
        }
        res += right - left + 1
    }
    return res
}