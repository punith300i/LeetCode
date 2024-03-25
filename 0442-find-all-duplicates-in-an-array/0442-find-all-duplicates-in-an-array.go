func findDuplicates(nums []int) []int {
    var result *[]int = &[]int{}
    
    for _, num := range nums{
        index := abs(num) - 1
        if nums[index]<0 {
            *result = append(*result, abs(num))
        }
        nums[index] = -nums[index]
    }
    
    return *result
}
func abs(value int) int {
    if value < 0{
        return -value
    }
    return value
}