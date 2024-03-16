func fib(n int) int {
    var dp = make([]int, n)
    
    if n<2 {
        return n
    }
    
    dp[0]=1
    dp[1]=1
    for i := range n{
        if i>1{
            dp[i] = dp[i-1] + dp[i-2]
        }
    }
    return dp[len(dp)-1]
}