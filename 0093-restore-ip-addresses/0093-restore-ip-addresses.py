class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def rec(i , addr):
            
            if i == len(s):
                if len(addr)==4:
                    res.append(".".join(map(str,addr)))
                return
            
            if addr[-1]!=0 and addr[-1]*10+int(s[i]) <= 255:
                last_element = addr[-1]
                addr[-1] = last_element*10 + int(s[i])
                rec(i+1, addr)
                addr[-1] = last_element
            
            if len(addr)<4:
                rec(i+1, addr + [int(s[i])])
        
        rec(1, [int(s[0])])
        return res
                    