class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events = []
        @cache
        def solve( i, k):
            if i >= len(self.events): 
                return 0
            if k <= 0: 
                return 0
            s, e, v = self.events[i]
            j = bisect.bisect(self.events, [e+1])
            return max(v + solve(j, k - 1), solve(i + 1, k))
        events.sort() 
        self.events = events
        return solve(0, k)
    