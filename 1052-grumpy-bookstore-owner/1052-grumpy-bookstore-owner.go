func maxSatisfied(customers []int, grumpy []int, minutes int) int {
    ans := 0
    total := 0
    n := len(customers)

    for i := 0; i < n; i++ {
        total += (1 - grumpy[i]) * customers[i]
    }

    windowAll := 0
    windowPartial := 0
    for i := 0; i < n; i++ {
        windowAll += customers[i]
        windowPartial += (1 - grumpy[i]) * customers[i]
        if i + 1 >= minutes {
            ans = max(ans, total - windowPartial + windowAll)
            left := i - minutes + 1
            windowAll -= customers[left]
            windowPartial -= (1 - grumpy[left]) * customers[left]
        }
    }

    return ans
}