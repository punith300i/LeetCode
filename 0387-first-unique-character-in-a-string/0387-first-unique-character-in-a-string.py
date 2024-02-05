class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for element_index in range(len(s)):
            if counter[s[element_index]] == 1:
                return element_index
        return -1