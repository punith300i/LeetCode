# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return 
        
        queue = deque()
        
        queue.append(root)
        
        res = []
        while queue:
            temp = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(temp)
        
        return res[::-1]