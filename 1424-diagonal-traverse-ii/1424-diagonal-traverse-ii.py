class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d_map = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d_map[i+j].append(nums[i][j])
        
        result = []
        for values in d_map.values():
            result+=values[::-1]
            
        return result