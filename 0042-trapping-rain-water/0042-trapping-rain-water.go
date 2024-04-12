func trap(height []int) int {
    
    if len(height) <= 1 {
        return 0
    }
    
    l := len(height)
    dpLeft := make([]int, l)
    dpRight := make([]int, l)
    
    dpLeft[0] = height[0]    
    for i := 1; i < l; i++ {
        dpLeft[i] = max(dpLeft[i-1], height[i])
    }
    
    dpRight[l-1] = height[l-1]
    for i := l - 2; i >=0 ; i-- {
        dpRight[i] = max(dpRight[i+1], height[i])
    }
    
    res := 0
    for i := 0; i < l; i++ {
        if dpLeft[i] > height[i] && dpRight[i] > height[i] {
            res += min(dpLeft[i], dpRight[i]) - height[i]
        }
    }
    return res
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}