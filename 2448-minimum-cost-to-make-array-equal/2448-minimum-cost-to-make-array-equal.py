class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def compute_cost(val):
            total_cost = 0
            for i in range(len(nums)):
                total_cost+= abs(val-nums[i]) * cost[i]
            return total_cost
        
        left = min(nums)
        right = max(nums)
        result = compute_cost(nums[0])
        
        while left<right:
            
            mid = left + (right-left)//2

            if compute_cost(mid)>compute_cost(mid+1):
                left = mid+1
                result = compute_cost(left)
            else:
                right = mid
                result = compute_cost(right)
        
        return result
                