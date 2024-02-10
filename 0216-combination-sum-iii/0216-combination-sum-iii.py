class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def rec_func(index, lst, target):
            if target == 0 and len(lst)==k:
                res.append(lst.copy())
            
            
            for i in range(index,10):
                if i<=target:
                    lst.append(i)
                    rec_func(i+1, lst, target-i)
                    lst.pop()
                
        
        rec_func(1,[],n)
        return res