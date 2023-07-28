class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        dpArray=[[[0,0] for i in range(len(nums))] for j in range(len(nums))]

        for i in range(len(nums)):
            dpArray[i][i]=[nums[i],0]
        
        for l in range(2,len(nums)+1):
            for i in range(0,len(nums)-l+1):
                j=i+l-1
                dpArray[i][j][0] = max(nums[i]+dpArray[i+1][j][1],nums[j]+dpArray[i][j-1][1])
                dpArray[i][j][1] = min(dpArray[i+1][j][0],dpArray[i][j-1][0])
        
        return dpArray[0][-1][0]>=dpArray[0][-1][1]