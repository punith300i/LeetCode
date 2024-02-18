class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings,key=itemgetter(0))
        freeRooms = []
        endTimes = []
        noOfTimesRoomUsed = [0] * n
        for i in range(n):
            heapq.heappush(freeRooms,(i))
        
        for start, end in meetings:
            while len(endTimes) > 0 and start >= endTimes[0][0]:
                free = heapq.heappop(endTimes)
                heapq.heappush(freeRooms,(free[1]))
            
            heapq.heapify(freeRooms)

            if len(freeRooms) > 0:
                room = heapq.heappop(freeRooms)
                noOfTimesRoomUsed[room] += 1
                heapq.heappush(endTimes, (end,room))
                print(end,room)
            else:
                released = heapq.heappop(endTimes)
                diff = 0
                if released[0] > start:
                    diff = released[0] - start

                noOfTimesRoomUsed[released[1]] += 1
                heapq.heappush(endTimes, (end+diff, released[1])) 
            
            heapq.heapify(endTimes)
        
        return noOfTimesRoomUsed.index(max(noOfTimesRoomUsed))
