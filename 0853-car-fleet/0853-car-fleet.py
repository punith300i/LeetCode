class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dist = [target - pos for pos in position]
        time = [dist[i]/speed[i] for i in range(len(position))]
        
        stack = []
        
        dist_time = [[position[i],time[i]] for i in range(len(position))]
        
        for d,t in sorted(dist_time, key= lambda x: x[0], reverse=True):
            stack.append([d,t])
            if len(stack)>=2 and stack[-1][1] <= stack[-2][1]:
                stack.pop()
        
        return len(stack)
            