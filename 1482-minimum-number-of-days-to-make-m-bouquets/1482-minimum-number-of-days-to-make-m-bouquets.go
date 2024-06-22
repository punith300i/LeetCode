func minDays(bloomDay []int, m int, k int) int {
    // impossible condition
    if m*k > len(bloomDay){
        return -1
    }
    
    left := 0
    right := slices.Max(bloomDay)
    
    answer:=-1
    
    // Binary Search on answer approach 
    for left <= right {
        mid := left + (right - left)/2
        
        // check the number of bouquets we can make with mid number of days
        bcnt:=0
        cnt:=0
        for _, day := range bloomDay{
            // if the flower is already bloomed else count 0 as we don't have any adj flowers
            if day<=mid{
                cnt++
            }else{
                cnt=0
            }
            
            // count bouquets if we have them as k adjacent flowers.
            if cnt==k{
                bcnt++
                cnt=0
            }
        }
        
        // if we have enough bouquet counts, our answer will be in the left half and we reject right half
        if bcnt >= m{
            answer = mid
            right = mid-1
        }else{
            left = mid+1
        }
    }
    
    return answer
}