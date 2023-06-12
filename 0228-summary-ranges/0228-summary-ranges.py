class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(9999)
        start = nums[0]
        result = []
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                end = nums[i-1]
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = nums[i]
            if i==len(nums):
                end = nums[i]
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                
        return result