class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i])
            if (i+1)%3==0:
                if temp[-1] - temp[0] <=k:
                    result.append(temp)
                else:
                    return []
                temp=[]
        return result
            
                    
                       
                
            