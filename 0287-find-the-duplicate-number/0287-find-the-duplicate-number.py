class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v>1:
                break
        return k