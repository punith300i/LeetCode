class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low = 1
        high = max(quantities)
        
        while(low<=high):
            mid = low + (high - low)//2
            
            req_stores = 0
            for quantity in quantities:
                temp = quantity
                while(temp>0):
                    temp-=mid
                    req_stores+=1
            
            if req_stores <= n:
                high = mid-1
            else:
                low = mid+1
    
        return low
            