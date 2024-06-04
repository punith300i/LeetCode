func longestPalindrome(s string) int {
    count := make([]int, 128)
    for _, v := range s {
        count[v]++
    }
    
    ans := 0
    for _, v := range count {
        ans += v/2*2
        if ans % 2 == 0 && v % 2 == 1 {
            ans++
        }
    }
    return ans
}