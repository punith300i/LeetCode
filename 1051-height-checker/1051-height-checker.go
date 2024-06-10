func heightChecker(heights []int) int {
    sorted_heights := make([]int, len(heights))
    copy(sorted_heights, heights)
    sort.Ints(sorted_heights)
    ans := 0
    for i := 0; i < len(heights); i++ {
        if sorted_heights[i] != heights[i] {
            ans++
        }
    }
    return ans
}