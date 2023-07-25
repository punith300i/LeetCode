class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        
        l = 0 
        r = len(a) - 1
        
        while l <= r:
            mid = (l+r)//2
            
            if a[mid+1]<a[mid] and a[mid]>a[mid-1]:
                return mid
            
            if a[mid+1] > a[mid]:
                l = mid+1
            else:
                r = mid
        