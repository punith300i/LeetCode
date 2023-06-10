class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while(i<=j):
            max_area = max(max_area, min(height[i],height[j]) * (j-i))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return max_area
