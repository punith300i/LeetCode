class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        num_frequency = Counter(nums)
        nums = sorted(num_frequency.keys())[::-1]
        result = 0
        for i in range(1, len(nums)):
            result+=num_frequency[nums[i-1]]
            num_frequency[nums[i]]+=num_frequency[nums[i-1]]
        return result
            