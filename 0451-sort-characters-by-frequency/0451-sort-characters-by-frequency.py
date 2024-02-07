class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        freq_tuple = [(letter, index) for letter,index in counter.items()]
        sorted_list = sorted(freq_tuple, key=lambda x: -x[1])
        res = ""
        for letter,count in sorted_list:
            res+=letter*count
        return res