class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec_func(index,lst):
            if index == len(nums):
                res.append(nums[:])
                return
            
            for i in range(index,len(nums)):
                nums[i],nums[index] = nums[index],nums[i]
                rec_func(index+1, nums.copy())
                nums[i],nums[index] = nums[index],nums[i]
                
        rec_func(0,[])
        return res
                    