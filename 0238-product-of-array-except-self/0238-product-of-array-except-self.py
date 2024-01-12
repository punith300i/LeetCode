class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        one_zero_product = 1
        zeros = 0
        
        for i in range(len(nums)): 
            if nums[i]==0:
                zeros+=1
            elif nums[i]!=0:
                one_zero_product = one_zero_product * nums[i]
            total_product = total_product*nums[i]
        
        for i in range(len(nums)):
            if zeros>1:
                nums[i]=0
                continue
            if nums[i]==0:
                nums[i] = one_zero_product
            else:
                nums[i] = total_product//nums[i]
                
        return nums