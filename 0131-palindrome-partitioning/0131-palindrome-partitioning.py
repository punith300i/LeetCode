class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def check_palindrome(s):
            return s == s[::-1]
        
        def rec_func(index, lst):
            nonlocal res
            
            if index == len(s):
                res.append(lst)
                return
            
            for j in range(index, len(s)):
                cur_res = s[index:j+1]
                if check_palindrome(cur_res):
                    rec_func(j+1, lst + [cur_res])
        
        rec_func(0,[])
        return res
                