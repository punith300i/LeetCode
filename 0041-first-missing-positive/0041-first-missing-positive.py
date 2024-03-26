class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        m = 1
        while m in nums:
            m+=1
        return m