class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        freq = {}
        for i in hand:
            freq[i] = 1+freq.get(i,0)
        
        heap = list(freq.keys())
        heapq.heapify(heap)
        
        while heap:
            min_element = heap[0]
            
            for i in range(min_element, min_element + groupSize):
                if i not in freq:
                    return False
                freq[i]-=1
                if freq[i]==0:
                    if i!=heap[0]:
                        return False
                    heapq.heappop(heap)
        return True