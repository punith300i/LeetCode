class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        
        pq = [(-count, char ) for char,count in Counter(s).items()]
        heapq.heapify(pq)
        
        while pq:
            count_f,char_f = heapq.heappop(pq)
            if not ans or char_f!=ans[-1]:
                ans.append(char_f)
                if count_f + 1 != 0:
                    heappush(pq, (count_f+1, char_f))
            else:
                if not pq: return ""
                count_s, char_s = heapq.heappop(pq)
                ans.append(char_s)
                if count_s + 1!=0:
                    heappush(pq, (count_s+1, char_s))
                heappush(pq, (count_f, char_f))
                
        return ''.join(ans)