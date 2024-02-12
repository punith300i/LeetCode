class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        freq = [0 for i in range(n+1)]
        dp = {}
        def rec_func(index,freq):
            if index == n+1:
                return 1
            
            #memo :
            if (index, tuple(freq)) in dp:
                return dp[(index, tuple(freq))]
            
            count = 0
            for i in range(1,n+1):
                if not freq[i]:
                    if i%index == 0 or index%i==0:
                        freq[i]=1
                        count+=rec_func(index+1,freq)
                        freq[i]=0
                        
            dp[(index, tuple(freq))] = count
            return count
        
        return rec_func(1,freq)