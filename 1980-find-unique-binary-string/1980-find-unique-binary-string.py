class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = []
        width = len(nums[0])
        for i in nums:
            n.append(int(i,2))
        for i in range((max(n)+2)*2):
            if i not in n:
                return "{:0{width}b}".format(i, width=width)
        return -1