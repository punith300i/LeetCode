class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left_range = index
        right_range = n-index-1
        
        low = 1
        high = maxSum
        
        result = 0
        
        while low<=high:
            
            mid = (high-low)//2 + low
            range_element = mid-1
            
            if(left_range <= range_element):
                left_sum = (range_element*(range_element+1))//2 - ((range_element-left_range)*(range_element-left_range+1))//2
            else:
                left_sum =  (range_element*(range_element+1))//2 + left_range - range_element
                                                                   
            if(right_range <= range_element):
                right_sum = (range_element*(range_element+1))//2 - ((range_element-right_range)*(range_element-right_range+1))//2
            else:
                right_sum =  (range_element*(range_element+1))//2 + right_range - range_element
                                                                              
            total_sum = left_sum + mid + right_sum

            if total_sum <= maxSum:
                low = mid+1
                result = mid
            else:
                high = mid-1
    
        return result
                                     
            