class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = collections.defaultdict(list)
        
        for i in range(len(edges)):
            s,d = edges[i]
            graph[s].append((d,succProb[i]))
            graph[d].append((s,succProb[i]))
            
        pq = [(-1,start)]
        visited = set()
        
        while pq:
            
            cur_prob, cur_node = heapq.heappop(pq)
            visited.add(cur_node)
            
            if cur_node == end:
                return -1*cur_prob
            
            for adj_node, adj_prob in graph[cur_node]:
                if adj_node not in visited:
                    heapq.heappush(pq,(adj_prob*cur_prob, adj_node))
        
        return 0