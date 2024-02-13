class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = 1
        lst = []
        res = ""
        for i in range(1,n):
            factorial = factorial * i
            lst.append(i)
        
        lst.append(n)
        k-=1
        
        while(True):
            res = res + str(lst[int(k//factorial)])
            lst.remove(lst[int(k//factorial)])
            
            if len(lst) == 0:
                break
                
            k = k % factorial
            factorial = factorial/len(lst)
        
        return res
            