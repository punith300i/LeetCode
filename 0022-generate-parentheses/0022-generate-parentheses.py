class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        result = []
        
        def backtrack(open_b,close_b):
            if open_b == close_b == n:
                result.append("".join(stack))
                return
            
            if open_b < n:
                stack.append('(')
                backtrack(open_b+1, close_b)
                stack.pop()
            
            if close_b < open_b:
                stack.append(')')
                backtrack(open_b, close_b+1)
                stack.pop()
        
        backtrack(0,0)
        return result