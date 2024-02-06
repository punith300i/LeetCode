class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def rec_func(index, lst, s):
            nonlocal res
            
            if s == 0:
                res.add(tuple(lst))
                return
            
            for i in range(index,len(candidates)):
                if i> index and candidates[i] == candidates[i-1]: continue
                if candidates[i] <= s:
                    lst.append(candidates[i])
                    rec_func(i+1, lst, s-candidates[i])
                    prev = lst.pop()
        
        candidates.sort()
        rec_func(0,[],target)
        return res