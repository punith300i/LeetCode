class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        result = low
        while(low<=high):
            mid = low + (high - low)//2
            mid_req_days = 0
            temp = 0
            for weight in weights:
                temp += weight
                if temp>mid:
                    temp = 0 
                    temp+=weight
                    mid_req_days+=1
            mid_req_days+=1            
            if mid_req_days <= days:
                high = mid-1
                result = mid
            else:
                low = mid+1
                
        return result