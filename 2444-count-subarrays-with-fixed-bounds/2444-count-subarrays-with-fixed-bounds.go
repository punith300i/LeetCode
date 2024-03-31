func countSubarrays(nums []int, minK int, maxK int) int64 {
    var minkPos, maxkPos int = -1, -1
    var left int = 0
    
    var result int64 = 0
    
    for right:=0; right<len(nums); right++{
        // outside the range
        if nums[right] < minK || nums[right] > maxK {
            // reset the positions
            left = right + 1
            minkPos = -1
            maxkPos = -1
        }else{
            // case when the it is in the min-max k range
            // update min and max positions
            if nums[right]==minK{
                minkPos = right
            }
            if nums[right]==maxK{
                maxkPos = right
            }
             
        }
        
        result += int64(max(0,min(minkPos, maxkPos)-left + 1))
 
    }
    
    return result
}