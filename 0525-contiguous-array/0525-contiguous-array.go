func findMaxLength(nums []int) int {
    hashMap := make(map[int]int)
    hashMap[0]=-1
    
    prefixSum := 0
    
    maxLength := 0
    
    for i := range nums{
        if nums[i]==0 {
            prefixSum--
        }else{
            prefixSum++
        }
        
        if val, ok := hashMap[prefixSum]; ok {
            if (i-val) > maxLength{
                maxLength = i-val
            }
        }else{
                hashMap[prefixSum]=i
            }
    }
    
    return maxLength
}