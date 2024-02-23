class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        price = defaultdict(int)
        for s, d, val in flights:
            graph[s].append(d)
            price[(s,d)] = val
        
        
        cost = [float('inf') for i in range(n)]
        queue = deque()
        
        queue.append((src, 0))
        cost[src] = 0
        while queue and k>=0:
            # traverse at each level and fill shortest distance
            for i in range(len(queue)):
                src, cost_to_reach = queue.popleft()
                for node in graph[src]:
                    if cost_to_reach + price[(src,node)] < cost[node]:
                        cost[node] = cost_to_reach + price[(src,node)]
                        queue.append((node,cost[node]))
            k-=1
        
        return cost[dst] if cost[dst]!=float('inf') else -1