class Solution:
    def pivotInteger(self, n: int) -> int:
        l = 0
        r = n
        while l<=r:
            mid = l + (r-l)//2
            left_sum = sum(range(1,mid+1))
            right_sum = sum(range(mid,n+1))
            
            if left_sum == right_sum:
                return mid
            
            if left_sum > right_sum:
                r = mid-1
            else:
                l = mid+1
        
        return -1
        