class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1]*n
        def recursive_function(index: int) -> any:
            
            # base case
            if index == n:
                return 0
            
            # memoization
            if dp[index] != -1:
                return dp[index]
                
            length = 0
            subarray_maximum = float('-inf')
            maximum_sum = float('-inf')
            
            for j in range(index, min(index+k,n)):
                length+=1
                subarray_maximum = max(subarray_maximum, arr[j])
                sum_so_far = length * subarray_maximum + recursive_function(j+1)
                maximum_sum = max(maximum_sum, sum_so_far)
            
            dp[index] = maximum_sum
            return dp[index]
        
        return recursive_function(0)