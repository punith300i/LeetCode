class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        time = 0
        heapq.heapify(heap)
        q = deque()
        
        while heap or q:
            time+=1
            
            if heap:
                cnt = 1+heapq.heappop(heap)
                if cnt:
                    q.append((time, cnt))
            
            if q and q[0][0] + n == time:
                heapq.heappush(heap, q.popleft()[1])
        
        return time
            
            