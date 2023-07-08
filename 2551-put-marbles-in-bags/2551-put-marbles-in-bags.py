class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        if len(weights)==k:
            return 0
        
        pair_sum = []
        for i in range(1,len(weights)):
            pair_sum.append(weights[i]+weights[i-1])
        
        pair_sum.sort()
        
        max_sum = 0
        min_sum = 0
        
        for i in range(k-1):
            max_sum += pair_sum[len(pair_sum)-i-1]
            min_sum += pair_sum[i]

        return max_sum - min_sum