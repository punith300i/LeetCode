class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        from typing import Set
        str_len = len(nums[0])
        nums = set(nums)
        result = []
        def rec_solve(rel_length: int, cur_string:str) -> str | None:
            if rel_length <=0 :
                if cur_string not in nums:
                    result.append(cur_string)
                return
            rec_solve(rel_length-1, cur_string=cur_string+'0')
            rec_solve(rel_length-1, cur_string=cur_string+'1')
            return 
        rec_solve(rel_length=str_len,cur_string="")
        return result[0]
        