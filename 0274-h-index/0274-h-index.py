class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations)-i:
                ans = max(ans,len(citations)-i)
        return ans