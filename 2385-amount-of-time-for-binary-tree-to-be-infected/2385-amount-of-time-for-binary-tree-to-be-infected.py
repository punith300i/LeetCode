# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # variables
        graph = defaultdict(list)
        result = 0
        
        # Pre-Order traversal to generate graph
        def create_graph(root):
            if root is None:
                return 
            if root.left is not None:
                graph[root.left.val].append(root.val)
                graph[root.val].append(root.left.val)
            if root.right is not None:
                graph[root.right.val].append(root.val)
                graph[root.val].append(root.right.val)
        
            create_graph(root.left)
            create_graph(root.right)
        
        # Generate graph
        create_graph(root)
        
        # BFS Traversal
        queue = deque()
        queue.append((start,0))
        visited = set()
        height = 0
        
        while len(queue)>0:
            val,height = queue.popleft()
            visited.add(val)
            result = max(result, height)
            
            for node in graph[val]:
                if node not in visited:
                    queue.append((node,height+1))
        
        return result