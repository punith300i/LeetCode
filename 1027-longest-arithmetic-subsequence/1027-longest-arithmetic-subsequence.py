class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[(i,diff)] = dp.get((j,diff),1)+1
                res = max(res,dp[(i,diff)])
        return res