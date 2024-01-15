class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scounter = Counter(s)
        tcounter = Counter(t)
        result = 0
        for k in scounter:
            if k in tcounter:
                result += max(scounter[k] - tcounter[k],0)
            else:
                result += scounter[k]
        return result
            