func firstMissingPositive(nums []int) int {
    var hmap = map[int]bool{}
    for _, val := range nums{
        hmap[val]=true
    }
    var m int = 1
    for{
        if _, ok := hmap[m]; !ok {
            return m
        }
        m++
    }
    return 1
}