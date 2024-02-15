class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<3:
            return -1
        nums.sort()
        perimeter=sum(nums)
        for i in range(1,len(nums)-1):
            longest=nums[-i]
            if perimeter - 2*longest>0:
                return perimeter
            else:
                perimeter-=longest
        else:
            return -1     
                