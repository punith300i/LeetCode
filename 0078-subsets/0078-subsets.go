var Result [][]int = [][]int{}

func subsets(nums []int) [][]int {
    Result = [][]int{}
    RecFunc(0,[]int{}, nums)
    return Result
}

func RecFunc(index int, subset []int,  nums []int) {
    if index == len(nums){
        copySubset := make([]int, len(subset))
        copy(copySubset, subset)
        Result = append(Result, copySubset)
        return
    }
    
    RecFunc(index+1, append(subset, nums[index]), nums)
    RecFunc(index+1, subset, nums)
}