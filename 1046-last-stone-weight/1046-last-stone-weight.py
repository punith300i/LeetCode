class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x!=y:
                heapq.heappush(stones,-abs(x-y))
        return -stones[0] if len(stones)>0 else 0
            