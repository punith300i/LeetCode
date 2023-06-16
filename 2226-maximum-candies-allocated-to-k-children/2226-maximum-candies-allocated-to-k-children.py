class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = max(candies)
        result = 0
        
        while(low<=high):
            
            mid = low + (high-low)//2
            
            children_count = 0
            for i in candies:
                children_count += i//mid
                
            if children_count>=k:
                low = mid+1
                result = mid
            else:
                high = mid-1
                
        return result