class Solution:
    def distance(self,p1,p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        heapq.heapify(heap)

        for point in points:
            heapq.heappush(heap, (self.distance((0,0),point),point))
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result