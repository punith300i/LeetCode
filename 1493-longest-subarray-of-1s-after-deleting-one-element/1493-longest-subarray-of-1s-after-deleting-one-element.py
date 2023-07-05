class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        def get_answer(index):
            answer = 0
            l = index-1
            n = len(nums)
            while l>=0 and nums[l]!=0:
                answer+=1
                l-=1
            r = index+1
            while r<n and nums[r]!=0:
                answer+=1
                r+=1
            return answer
        
        result = -float('inf')

        for i in range(len(nums)):
            if nums[i]==0:
                result = max(result, get_answer(i))
        
        return len(nums)-1 if result == -float('inf') else result 