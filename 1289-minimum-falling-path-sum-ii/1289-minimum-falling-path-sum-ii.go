func minFallingPathSum(grid [][]int) int {
    if len(grid) == 1 {
        return grid[0][0]
    }
    
    minVal := 0
    minPos := -1
    prevMin := 0
    
    for _, row := range grid {
        // Since the maximum path sum would be 99 * 200 = 19800, set initital min values to max + 1
        newMin := 19801
        newMinPos := 0
        newPrevMin := 19801
        
        for i, val := range row {
            if i == minPos {
                val += prevMin
            } else {
                val += minVal
            }
            
            if val < newMin {
                newPrevMin = newMin
                newMin = val
                newMinPos = i
            } else if val < newPrevMin {
                newPrevMin = val
            }
        }
        minVal = newMin
        minPos = newMinPos
        prevMin = newPrevMin
    }
    return minVal
}