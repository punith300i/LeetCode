class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        if len(arr)<2:
            return True
        
        diff = abs(arr[0] - arr[1])
        
        for i in range(1,len(arr)-1):
            if(abs(arr[i]-arr[i+1]) != diff):
                return False
        
        return True