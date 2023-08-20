class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        lastpos = 0
        maxpos = 0
        jumps = 0
        while(lastpos<n-1):
            maxpos = max(maxpos, i + nums[i])
            if i==lastpos:
                lastpos = maxpos
                jumps+=1
            i+=1
        return jumps
                