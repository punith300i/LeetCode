class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        res = 0
        for i in intervals[1:]:
            if end <= i[0]:
                end = i[1]
            else:
                res+=1
                end = min(end,i[1])
        return res