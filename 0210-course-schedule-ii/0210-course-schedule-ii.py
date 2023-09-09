class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        queue = deque()
        
        for node in range(numCourses):
            if indegree[node]==0:
                queue.append(node)
        
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for adj_node in graph[node]:
                indegree[adj_node]-=1
                if indegree[adj_node]==0:
                    queue.append(adj_node)
        
        return result if len(result)==numCourses else []
            
            