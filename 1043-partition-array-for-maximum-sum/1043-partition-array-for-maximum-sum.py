class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for index in range(n)[::-1]:
            length = 0
            subarray_maximum = float('-inf')
            maximum_sum = float('-inf')
            
            for j in range(index, min(index+k,n)):
                length+=1
                subarray_maximum = max(subarray_maximum, arr[j])
                sum_so_far = length * subarray_maximum + dp[j+1]
                maximum_sum = max(maximum_sum, sum_so_far)
            
            dp[index] = maximum_sum
        return dp[0]
        