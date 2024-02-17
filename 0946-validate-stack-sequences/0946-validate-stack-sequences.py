class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i=0
        for val in pushed:
            stk.append(val)
            while len(stk)>0 and stk[-1] == popped[i]:
                stk.pop()
                i+=1
        return len(stk)==0