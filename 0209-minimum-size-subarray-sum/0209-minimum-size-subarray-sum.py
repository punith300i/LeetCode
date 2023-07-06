class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        sums=0
        res=float('inf')
        for r in range(len(nums)):
            sums+=nums[r]
            
            while sums>=target:
                res = min(res,r-l+1)
                sums=sums-nums[l]
                l+=1
        return res if res!=float('inf') else 0