class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = [n - int(str(n)[::-1]) for n in nums]
        result = 0
        for val in Counter(nums).values():
            result += val * (val-1)//2
        return result % (10**9 + 7)