class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent = [i for i in range(n+1)]

        def find(node):

            while node!=parent[node]:
                node=parent[node]

            return node 

        def union(i,j):
            pi = find(i)
            pj = find(j)

            parent[pj]=pi

        for s,d in edges:
            if find(s)== find(d):
                return [s,d]
            else:
                union(s,d)
