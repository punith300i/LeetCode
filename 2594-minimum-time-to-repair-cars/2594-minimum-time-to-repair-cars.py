class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = cars * cars * max(ranks)
        
        while(low<=high):
            mid = low + (high-low)//2
            
            req_cars = 0
            for car_rank in ranks:
                req_cars += int(sqrt(mid//car_rank))
            
            if req_cars >= cars:
                high = mid - 1
            else:
                low = mid + 1
            
        return high+1
            