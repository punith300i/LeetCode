class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, n, k, temp, ans):
            if k == 0:
                ans.append(temp[:])
                return
            if i == n:
                return
            dfs(i + 1, n, k, temp, ans)
            temp.append(i + 1)
            dfs(i + 1, n, k - 1, temp, ans)
            temp.pop()

        ans = []
        temp = []
        dfs(0, n, k, temp, ans)
        return ans