func findTargetSumWays(nums []int, target int) int {
    dp := map[MyData]int{}
    return RecFunc(0, 0, &nums, target, &dp)
}

type MyData struct {
    index int
    total int
}

func RecFunc (index int, total int, numsP *[]int, target int, dp *map[MyData]int) int {
    if index == len(*numsP){
        if total == target {
            return 1
        }else{
            return 0
        }
    }
    
    key := MyData{index, total}
    
    if _, ok := (*dp)[key]; !ok {
        pos := RecFunc(index+1, total+ (*numsP)[index], numsP, target, dp)
        neg := RecFunc(index+1, total+ (-1 *(*numsP)[index]), numsP, target, dp)
        
        (*dp)[key] = pos + neg
    }
    
    return (*dp)[key]
}