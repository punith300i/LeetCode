func maximumHappinessSum(happiness []int, k int) int64 {
    var max int64
    sort.Ints(happiness)
    lenIdx := len(happiness)-1
    dec := 0
    for k > 0 {
        happiness[lenIdx] -= dec
        if happiness[lenIdx] <= 0 {
            break
        }
        max += int64(happiness[lenIdx])

        k--
        lenIdx--
        dec++
    }

    return max
}