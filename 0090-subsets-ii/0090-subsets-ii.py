class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec_func(index, lst):
            
            if index>len(nums):
                return
            
            res.append(lst.copy())
            
            for i in range(index, len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                lst.append(nums[i])
                rec_func(i+1, lst.copy())
                lst.pop()
                
        nums.sort()
        rec_func(0,[])
        
        return res