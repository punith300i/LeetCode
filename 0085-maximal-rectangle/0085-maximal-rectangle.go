func maximalRectangle(matrix [][]byte) int {
    if len(matrix) == 0 || len(matrix[0]) == 0 { return 0 }
    row := len(matrix)
    col := len(matrix[0])
    heights := make([]int, col)
    res := 0
    for i := 0; i < row; i++ {
        for j := 0; j < col; j++ {
            if matrix[i][j] == '1' {
                heights[j] = heights[j] + 1
            } else {
                heights[j] = 0
            }
        }
        tmp := largestRectangleArea(heights)
        res = max(res, tmp)
    }
    return res
}

func largestRectangleArea(heights []int) int {
    if len(heights) == 0 { return 0 }
    lessFromLeft := make([]int, len(heights))
    lessFromRight := make([]int, len(heights))
    lessFromLeft[0] = -1
    lessFromRight[len(heights) - 1] = len(heights)
    for i := 1; i < len(heights); i++ {
        p := i - 1
        for p >= 0 && heights[p] >= heights[i] {
            p = lessFromLeft[p]
        }
        lessFromLeft[i] = p
    }
    for i := len(heights) - 2; i >= 0; i-- {
        p := i + 1
        for p < len(heights) && heights[p] > heights[i] {
            p = lessFromRight[p]
        }
        lessFromRight[i] = p
    }
    maxArea := 0
    for i := 0; i < len(heights); i++ {
        maxArea = max(maxArea, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))
    }
    return maxArea
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}