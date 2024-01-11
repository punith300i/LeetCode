class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        def backtrack(i, subset):
            
            if i == len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            
            subset.pop()
            
            backtrack(i+1, subset)
            
            return
            
        backtrack(0, [])
        return list(map(list,res))
            
        