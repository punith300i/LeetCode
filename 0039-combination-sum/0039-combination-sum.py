class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def rec_func(index,lst,s):
            nonlocal res
            
            if s > target:
                return
            
            if index == len(candidates):
                if s==target:
                    res.append(lst.copy())
                return
            
            lst.append(candidates[index])
            rec_func(index, lst, s+candidates[index])
            lst.pop()
            rec_func(index+1, lst, s)
        
        rec_func(0,[],0)
        return res