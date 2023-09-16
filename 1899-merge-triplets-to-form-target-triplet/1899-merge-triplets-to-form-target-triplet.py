class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        f1,f2,f3 = False, False, False
        for a,b,c in triplets:
            if a<=x and b<=y and c<=z:
                if a==x:
                    f1 = True
                if b==y:
                    f2 = True
                if c==z:
                    f3 = True
        return f1 and f2 and f3