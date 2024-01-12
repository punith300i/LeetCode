class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # using kadane by traversing in both directions
        
        max_prod = -999999
        cur_prod = 1
        for i in range(len(nums)):
            cur_prod = cur_prod * nums[i]
            max_prod = max(max_prod, cur_prod)
            if cur_prod == 0:
                cur_prod = 1
        
        cur_prod = 1
        nums = nums[::-1]
        for i in range(len(nums)):
            cur_prod = cur_prod * nums[i]
            max_prod = max(max_prod, cur_prod)
            if cur_prod == 0:
                cur_prod = 1
        
        return max_prod