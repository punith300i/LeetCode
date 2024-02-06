class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def rec_func(lst):
            if len(lst) == len(nums):
                res.add(tuple(lst.copy()))
                return
            
            for i in range(len(nums)):
                # if i>0 and nums[i]==nums[i-1]: 
                #     freq[i]=1
                #     continue
                    
                if not freq[i]:
                    freq[i]=1
                    lst.append(nums[i])
                    rec_func(lst.copy())
                    lst.pop()
                    freq[i]=0
                
        nums.sort()
        freq = [0]*len(nums)
        rec_func([])
        return res