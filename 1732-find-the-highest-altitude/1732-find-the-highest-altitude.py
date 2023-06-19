class Solution:
    def largestAltitude(self, gain: List[int]) -> int:       
        max_height = 0
        current_height = 0

        for i in gain:
            current_height +=i
            max_height = max(max_height,current_height)
        
        return max_height