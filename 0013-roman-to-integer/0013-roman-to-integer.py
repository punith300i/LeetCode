class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        res=0
        i=0

        while i<len(s):
            val=0
            if i<len(s)-1:
                if s[i:i+2]=='IV':
                    val= 4
                    i=i+2
                elif s[i:i+2]=='IX':
                    val= 9
                    i=i+2
                elif s[i:i+2]=='XL':
                    val= 40
                    i=i+2
                elif s[i:i+2]=='XC':
                    val= 90
                    i=i+2
                elif s[i:i+2]=='CD':
                    val= 400
                    i=i+2
                elif s[i:i+2]=='CM':
                    val= 900
                    i=i+2
                else:
                    val=d[s[i]]
                    i=i+1
            else:
                val=d[s[i]]
                i=i+1

            res=res+val
        return res