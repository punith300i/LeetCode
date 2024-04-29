func minOperations(nums []int, k int) int {
    total := nums[0]
    for i := 1; i < len(nums); i++ {
        total ^= nums[i]
    }
    diff := 0
    for i := 0; i < 32; i++ {
        if nBit(total, i) != nBit(k, i) {
            diff++
        }
    }
    return diff
}

func nBit(num int, i int) int {
    return num >> i & 1
}