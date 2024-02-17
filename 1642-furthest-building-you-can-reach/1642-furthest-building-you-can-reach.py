class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(heights)-1):
            difference = heights[i+1] - heights[i]
            
            # check postive difference
            if difference > 0:
                # push to heap if it can be accomodated with ladders
                heapq.heappush(heap,difference)
                
                # if it can't then see if bricks serves the purpose starting from min difference
                if len(heap) > ladders:
                    min_diff = heapq.heappop(heap)
                    bricks -= min_diff
                    
                    # if out of bricks return the index
                    if bricks<0:
                        return i
                
        
        return len(heights)-1