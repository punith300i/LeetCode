class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        self.indegree = [0] * numCourses
        self.res = []

        def build_graph(preq):
            for v,u in preq:
                self.graph[u].append(v)
                self.indegree[v]+=1
    
        build_graph(prerequisites)

        queue = deque()
        for node in range(numCourses):
            if self.indegree[node]==0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            self.res.append(node)

            for adj_node in self.graph[node]:
                self.indegree[adj_node]-=1
                if self.indegree[adj_node]==0:
                    queue.append(adj_node)
  
        return len(self.res)==numCourses