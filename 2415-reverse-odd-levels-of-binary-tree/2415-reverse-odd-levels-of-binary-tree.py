# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        queue = deque()
        
        queue.append(root)
        level = 0

        while queue:
            
            size = len(queue)
                       
            if level%2==1:
                l = 0
                r = size-1
                
                while l<r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l+=1
                    r-=1
            
            for _ in range(size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                    
            level+=1
            
        return root
        