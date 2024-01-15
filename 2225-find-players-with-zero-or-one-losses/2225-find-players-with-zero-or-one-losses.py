class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [0,0]
        winners = set(list(map(lambda x : x[0], matches)))
        losers = set(list(map(lambda x : x[1], matches)))
        
        answer[0] = sorted(list(winners-losers))
        l_counters = Counter(list(map(lambda x : x[1], matches)))
        answer[1] = sorted([k for k,v in l_counters.items() if v==1])
        
        return answer