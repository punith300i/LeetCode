# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def level_order_traversal(root):
            queue = deque()
            queue.append(root)  
            while queue:
                res = queue[0].val
                for i in range(len(queue)):
                    temp = queue.popleft()
                    if temp.left is not None:
                        queue.append(temp.left)
                    if temp.right is not None:
                        queue.append(temp.right)
            return res
        
        return level_order_traversal(root)