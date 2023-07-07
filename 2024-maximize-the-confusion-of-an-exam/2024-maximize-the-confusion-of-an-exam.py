class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def replace_lit(lit):
            l = 0
            counter = defaultdict(int)
            res = 0
            for r in range(len(answerKey)):
                counter[answerKey[r]]+=1
                
                while counter[lit]>k:
                    counter[answerKey[l]]-=1
                    l+=1
                
                res = max(res,r-l+1)
            
            return res
        
        return max(replace_lit('F'), replace_lit('T'))