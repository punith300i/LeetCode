class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = ""
        for i in range(len(s)):
            if len(stack) == 0 and s[i]==')':
                continue
            if s[i]=='(':
                stack.append('(')
            if len(stack)>0 and s[i]==')':
                stack.pop()
            result+=s[i]
        
        if len(stack)>0:
            for i in range(len(result))[::-1]:
                if result[i]=='(':
                    result = result[:i] + result[i+1:]
                    stack.pop()
                    if len(stack)==0:
                        break
        
        return result