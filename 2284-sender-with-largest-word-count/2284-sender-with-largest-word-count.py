class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hmap = dict()
        for i in range(len(senders)):
            hmap[senders[i]] = hmap.get(senders[i],0)+len(messages[i].split())
        max_val = max(hmap.values())
        res = ""
        for k,v in hmap.items():
            if v==max_val:
                res = max(res,k)
        return res
            