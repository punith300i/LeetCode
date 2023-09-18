class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stk1 = []
        stk2 = []
        
        if len(s)==1 and s[0]!="*":
            return False
        
        for i in range(len(s)):
            if s[i]=='(':
                stk1.append((s[i],i))
            elif s[i]=="*":
                stk2.append((s[i],i))
            else:
                if len(stk1)>0:
                    stk1.pop()
                elif len(stk2)>0:
                    stk2.pop()
                else:
                    return False
        
        if len(stk1) > len(stk2):
            return False
        
        if len(stk2) >= len(stk1) and len(stk1)>0:
            
            i,j=0,0
            
            while(i<len(stk1) and j<len(stk2)):
                if stk1[i][1] < stk2[j][1]:
                    i+=1
                    j+=1
                else:
                    j+=1
            if i < len(stk1):
                return False
        
        return True
            