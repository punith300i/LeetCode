class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        heapq.heapify(h)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(h) < k:
                     heapq.heappush(h, -1 * matrix[i][j])
                else:
                    if matrix[i][j] < -1 * h[0]:
                        heapq.heappop(h)
                        heapq.heappush(h, -1 * matrix[i][j])
                   
        return -1 * h[0]
                            
            