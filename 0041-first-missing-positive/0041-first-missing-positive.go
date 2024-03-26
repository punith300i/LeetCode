func firstMissingPositive(nums []int) int {
    for i := 0; i < len(nums); i++ {
        j := nums[i]
        for j >= 1 && j <= len(nums) {
            if nums[j - 1] > len(nums) || nums[j - 1] <= 0 || nums[j - 1] == j {
                nums[j - 1] = j
                break
            } else {
                temp := nums[j - 1]
                nums[j - 1] = j
                j = temp
            }
        }
    }
    //fmt.Println(nums)
    for i := 0; i < len(nums); i++ {
        if nums[i] != i + 1 {
            return i + 1
        }
    } 
    return len(nums) + 1
}