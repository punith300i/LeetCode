class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hmap = {}
        result = len(wall)
        for row in wall:
            cur_sum = 0
            for gap in row[:-1]:
                cur_sum+=gap
                hmap[cur_sum] = hmap.get(cur_sum,0)+1
                
        for value in hmap.values():
            result = min(result, len(wall)-value)
            
        return result