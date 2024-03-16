func fib(n int) int {
    var dp = make([]int, n+1)
    
    if n<1 {
        return n
    }
    
    dp[0]=0
    dp[1]=1
    for i := range n+1{
        if i>1{
            dp[i] = dp[i-1] + dp[i-2]
        }
    }
    return dp[len(dp)-1]
}