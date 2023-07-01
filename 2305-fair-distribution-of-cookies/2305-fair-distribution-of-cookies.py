class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        n = len(cookies)
        
        def dfs(i,zero_count):
            
            # if number of distributions to assign is less that the 
            # children not having cookies (zero_count)
            
            if n-i < zero_count:
                return float('inf')
            
            # if all the cookies are distributed
            if i==n:
                return max(distribution)
            
            answer = float('inf')
            # assigning cookies for all children
            for j in range(k):
                if distribution[j]==0:
                    zero_count-=1
                distribution[j]+=cookies[i]
                
                answer = min(answer, dfs(i+1, zero_count))
                
                # backtrack
                distribution[j]-=cookies[i]
                if distribution[j] == 0:
                    zero_count+=1
                    
            return answer
        
        return dfs(0,k)
                
                