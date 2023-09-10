class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        hmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for i in range(len(s)):
            if s[i] in hmap.values():
                stack.append(s[i])
            else:
                if len(stack)>0:
                    if hmap[s[i]] != stack.pop():
                        return False
                    
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
                