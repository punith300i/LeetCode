func threeConsecutiveOdds(arr []int) bool {
    sz := len(arr)
    
    if sz < 3 {return false}
    
    for i, _ := range arr {
        if i + 2 < sz {
            if arr[i] % 2 != 0 && arr[i + 1] % 2 != 0 && arr[i + 2] % 2 != 0 {
                return true
            }
        }        
    }
    
    return false
}