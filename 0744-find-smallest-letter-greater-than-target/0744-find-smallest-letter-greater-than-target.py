class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        result = letters[0]
        while l<=r:
            m = l + (r-l)//2
            
            if target >= letters[m]:
                l = m+1
            else:
                result = letters[m]
                r = m-1
        return result