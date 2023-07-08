class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,0
        res = []
        dq = deque()
        for r in range(len(nums)):
            
            while dq and nums[r]>nums[dq[-1]]:
                dq.pop()
            
            dq.append(r)

            if l > dq[0]:
                dq.popleft()

            if r+1 >= k:
                res.append(nums[dq[0]])
                l+=1

        return res