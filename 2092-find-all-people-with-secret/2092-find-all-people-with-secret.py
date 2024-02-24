class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        edges = defaultdict(list)
        for src, dst, time in meetings:
            edges[src].append((dst, time))
            edges[dst].append((src, time))
        earlist = defaultdict(lambda : float('inf'))
        pq = [(0, firstPerson), (0, 0)]
        while pq:
            curr_time, curr = heapq.heappop(pq)
            if curr_time > earlist[curr]:
                continue
            earlist[curr] = curr_time
            for neighbor, time in edges[curr]:
                if time >= curr_time and time < earlist[neighbor]:
                    earlist[neighbor] = time
                    heapq.heappush(pq, (time, neighbor))
        return earlist.keys()