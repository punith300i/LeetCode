class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]
            elif intervals[i][1] >= newInterval[0] or intervals[0][1]<= newInterval[0]:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        res.append(newInterval)
        return res