class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        freq = [0 for i in range(n+1)]
        def rec_func(index):
            if index == n+1:
                nonlocal res
                res+=1
                return
            
            for i in range(1,n+1):
                if not freq[i]:
                    if i%index == 0 or index%i==0:
                        freq[i]=1
                        rec_func(index+1)
                        freq[i]=0
        rec_func(1)
        return res