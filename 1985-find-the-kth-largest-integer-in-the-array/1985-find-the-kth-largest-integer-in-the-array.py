class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(lambda x: -int(x),nums))
        heapq.heapify(nums)
        for i in range(k):
            val = heapq.heappop(nums)
        return str(-val)
            
        