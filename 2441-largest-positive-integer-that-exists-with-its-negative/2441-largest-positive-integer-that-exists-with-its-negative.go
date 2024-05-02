func findMaxK(nums []int) int {
    var maxVal int = -1
    numsMap := make(map[int]bool)
    for _, val := range(nums){
        if _, ok := numsMap[val]; !ok{
            numsMap[val]=true
        }
    }
    for _, val := range(nums){
        if val > 0 && numsMap[-val] && val > maxVal{
            maxVal = val
        }
    }
    return maxVal
}