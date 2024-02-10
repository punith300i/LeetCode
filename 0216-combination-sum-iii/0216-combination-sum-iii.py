class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        
        def rec_func(index, lst, target):
            if index == k and target == 0:
                res.add(tuple(sorted(lst.copy())))
            
            for i in range(1,10):
                if i<=target:
                    if i not in lst:
                        lst.append(i)
                        rec_func(index+1, lst, target-i)
                        lst.pop()
        
        rec_func(0,[],n)
        return res