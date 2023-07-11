# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = defaultdict(list)

        self.res = []

        def build_graph(root):
            if root is None:
                return

            if root.left:
                self.graph[root.val].append(root.left.val)
                self.graph[root.left.val].append(root.val)
            if root.right:
                self.graph[root.val].append(root.right.val)
                self.graph[root.right.val].append(root.val)
            
            build_graph(root.left)
            build_graph(root.right)
        
        build_graph(root)
        
        queue = deque()

        visited = set()
        queue.append((target.val,0))
        
        visited.add(target.val)

        while len(queue) > 0:
            node, depth = queue.popleft()
            if depth == k:
                self.res.append(node)
            for adj_node in self.graph[node]:
                if adj_node not in visited:
                    queue.append((adj_node,depth+1))
                    visited.add(adj_node)

        return self.res
        

        