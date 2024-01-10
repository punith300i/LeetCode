class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = sum(piles)
        
        
        while (low<=high):
            mid = low + (high - low)//2
            req_hours = 0
            for pile in piles:
                req_hours += (pile+mid-1)//mid
            
            if req_hours <= h:
                high = mid-1
            else:
                low = mid+1
        
        return low