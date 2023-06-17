class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        arr2.sort()
        
        @cache
        def rec(i,x):
            
            if i==len(arr1):
                return 0
            
            j = bisect_left(arr2,x+1)
            
            swap = 1 + rec(i+1,arr2[j]) if j<len(arr2) else 2001
            no_swap = rec(i+1,arr1[i]) if arr1[i]>x else 2001
            
            return min(swap,no_swap)
            
        result = rec(0,-1)
        
        return result if result!=2001 else -1