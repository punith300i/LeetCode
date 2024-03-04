class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start = 0
        end = len(tokens)-1
        score = 0
        
        while start<=end:
            if tokens[start] <= power:
                power-=tokens[start]
                start+=1
                score+=1
            elif score>0:
                if start!=end:
                    power += tokens[end]
                    score-=1
                end-=1
            else:
                start+=1
        
        return score