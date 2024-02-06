class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec_func(lst):
            if len(lst) == len(nums):
                res.append(lst)
                return
            
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i]=1
                    lst.append(nums[i])
                    rec_func(lst.copy())
                    lst.pop()
                    freq[i]=0
                
                
        freq = [0]*len(nums)
        rec_func([])
        return res
                    