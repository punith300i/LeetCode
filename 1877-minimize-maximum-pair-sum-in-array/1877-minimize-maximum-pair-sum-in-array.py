class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_so_far = - float('inf')
        for i in range(1,len(sorted_nums)//2 +1):
            cur_max = sorted_nums[i-1] + sorted_nums[-i]
            max_so_far = max(cur_max, max_so_far)
        return max_so_far