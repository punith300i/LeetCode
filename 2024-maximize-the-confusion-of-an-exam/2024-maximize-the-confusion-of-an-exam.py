class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        l,r = 0,0
        counter = {}
        res = 0
        while r < len(answerKey):
            counter[answerKey[r]] = counter.get(answerKey[r],0)+1
            diff = r-l+1 - counter[max(counter,key=counter.get)]
            if diff > k:
                counter[answerKey[l]]-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res