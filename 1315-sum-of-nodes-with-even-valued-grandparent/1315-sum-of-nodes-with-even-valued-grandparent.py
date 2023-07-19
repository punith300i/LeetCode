# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        
        res = 0 
        
        queue = deque()
        
        queue.append((root, None, None))
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node, parent, gparent = queue.popleft()
                
                if gparent and gparent.val%2==0:
                    res+=node.val
                
                if node.left:
                    if parent is not None:
                        queue.append((node.left, node, parent))
                    else:
                        queue.append((node.left, node, None))
                if node.right:
                    if parent is not None:
                        queue.append((node.right, node, parent))
                    else:
                        queue.append((node.right, node , None))
        
        return res