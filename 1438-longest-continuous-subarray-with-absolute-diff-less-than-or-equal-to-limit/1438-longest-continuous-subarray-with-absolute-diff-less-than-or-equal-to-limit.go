func longestSubarray(nums []int, limit int) int {
    var mins, maxs []int
    start, end := 0, 0
    
    answer:=0
    for end < len(nums) {
        
        for len(mins)>0 && nums[mins[len(mins)-1]] >= nums[end]{
            mins = mins[:len(mins)-1]
        }
        
        for len(maxs)>0 && nums[maxs[len(maxs)-1]] <= nums[end]{
            maxs = maxs[:len(maxs)-1]
        }
        
        mins = append(mins, end)
        maxs = append(maxs, end)
        
        for start<end && abs(nums[mins[0]] - nums[maxs[0]]) > limit {
            start++
            
            // update dequeues
            for len(mins)>0 && mins[0] < start{
                mins = mins[1:]
            }
            
            for len(maxs)>0 && maxs[0] < start{
                maxs = maxs[1:]
            }
        }
        answer = max(answer, end-start+1)
        end++
        
    }
    
    return answer
}

func max(a,b int) int{
    if a<b{
        return b
    }else{
        return a
    }
}

func abs(a int) int{
    if a<0{
        return -a
    }
    
    return a
}