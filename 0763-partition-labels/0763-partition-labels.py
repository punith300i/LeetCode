class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = dict()
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = [i,i]
            else:
                hmap[s[i]][1] = max(hmap[s[i]][1],i)
        
        
        # merge intervals
        result = []
        
        intervals = list(hmap.values())
        running_val = intervals[0]
        for i in range(1,len(intervals)):
            current_val = intervals[i]
            if running_val[1]>=current_val[0]:
                running_val[0] = min(running_val[0], current_val[0])
                running_val[1] = max(running_val[1], current_val[1])
            else:
                result.append(running_val)
                running_val = current_val
        
        result.append(running_val)
        
        return list(map(lambda x: x[1]-x[0]+1, result))