class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = []
        visited = set()
        heapq.heappush(min_heap, (nums1[0]+nums2[0],0,0))
        visited.add((0,0))
        
        result = []
        
        while k>0 and min_heap:
            
            minsum,i,j = heapq.heappop(min_heap)
            result.append([nums1[i],nums2[j]])
            
            if (i+1,j) not in visited and i+1<len(nums1):
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))
            
            if (i,j+1) not in visited and j+1<len(nums2):
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))
            
            k-=1
        
        return result