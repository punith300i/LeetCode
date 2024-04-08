func findTargetSumWays(nums []int, target int) int {
    return RecFunc(0, 0, &nums, target)
}

func RecFunc (index int, total int, numsP *[]int, target int) int {
    if index == len(*numsP){
        if total == target {
            return 1
        }else{
            return 0
        }
    }
    
    pos := RecFunc(index+1, total+ (*numsP)[index], numsP, target)
    neg := RecFunc(index+1, total+ (-1 *(*numsP)[index]), numsP, target)
    
    return pos + neg
}