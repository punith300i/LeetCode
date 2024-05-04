func numRescueBoats(people []int, limit int) int {
    sort.Ints(people)
    i,j := 0, len(people) - 1
    ans := 0

    for ; i <= j; j-- {
        ans++
        if (people[i] + people[j] <= limit) { i++ }
    }

    return ans
}