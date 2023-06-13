class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r_set = defaultdict(int)
        result = 0
        for i in range(n):
            r_set["|".join(map(lambda x : str(x),grid[i]))]+=1
        for i in range(n):
            col_set = "|".join(map(lambda x : str(x),[row[i] for row in grid]))
            if col_set in r_set:
                result+=r_set[col_set]
        return result
