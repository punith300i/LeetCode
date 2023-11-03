class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        end = sum(piles)
        
        while(low <= end):
            mid = low + (end-low)//2
            req_hours = 0
            for pile in piles:
                req_hours += (pile + mid -1)//mid
            if req_hours <= h:
                end = mid-1
            else:
                low = mid+1
        
        return low