class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def counterCheck(string1: str, string2: str) -> bool:
            dict1 = {}
            
            for i in string1:
                if i not in dict1:
                    dict1[i] = 1
                else:
                    dict1[i]+=1
            
            for i in string2:
                if i not in dict1.keys():
                    return False
                else:
                    dict1[i]-=1
            
            for i in dict1.values():
                if i!=0:
                    return False
            
            return True
        
        for i in range(len(s2) - len(s1)+1):
            if counterCheck(s1,s2[i:i+len(s1)]):
                return True
        
        return False
                
            