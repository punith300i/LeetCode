class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec_func(index, lst):
            nonlocal res
            
            if index == len(nums):
                res.append(lst)
                return
            
            lst.append(nums[index])
            rec_func(index+1, lst.copy())
            lst.pop()
            rec_func(index+1, lst.copy())
            
        rec_func(0, [])
        return res