class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def rec_func(index, lst):
            nonlocal res
            
            if index == len(s):
                res.append(''.join(lst.copy()))
                return
            
            if s[index].isalpha():
                rec_func(index+1, lst + [s[index].lower()])
                rec_func(index+1, lst + [s[index].upper()])
            else:
                rec_func(index+1, lst + [s[index]])

        
        rec_func(0,[])
        return res