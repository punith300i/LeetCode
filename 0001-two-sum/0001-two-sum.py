class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hmap = dict()
        
        for i in range(n):
            hmap[nums[i]] = i
        
        for i in range(n):
            difference = target - nums[i]
            if difference in hmap.keys() and hmap[difference]!=i:
                return [i, hmap[difference]]
        
        return [0,0]