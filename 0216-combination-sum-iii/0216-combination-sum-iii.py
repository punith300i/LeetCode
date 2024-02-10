class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def rec_func(index, lst, s):
            if s == 0 and len(lst) == k:
                res.append(lst)
                return
            
            if index>=n or index>=10:
                return
            
            if index<=s:
                rec_func(index+1, lst+(index,), s-index)
            rec_func(index+1, lst, s)
        
        rec_func(1,tuple(),n)
        return res