class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1 = sorted(word1)
        word2 = sorted(word2)
        wsv1 = [v for k,v in Counter(word1).items()]
        wsv2 = [v for k,v in Counter(word2).items()]
        wsk1 = set([k for k,v in Counter(word1).items()])
        wsk2 = set([k for k,v in Counter(word2).items()])
        
        return sorted(wsv1)==sorted(wsv2) and wsk1 == wsk2