class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        lst = [(v,k) for k,v in counter.items()]
        heapq.heapify(lst)
        
        for i in range(k):
            value, key = heapq.heappop(lst)
            if value!=1:
                heapq.heappush(lst,(value-1, key))
        
        return len(lst)
                
            