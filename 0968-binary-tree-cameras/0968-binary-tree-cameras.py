# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = 0
        # 0 - node has camera
        # 1 - already monitired
        # -1 - need a camera
        def dfs(root):
            nonlocal res
            if root is None:
                return 1
            if root.left is None and root.right is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == -1 or right == -1:
                # add camera
                res+=1
                return 0
            
            if left == 0 or right == 0:
                return 1
            
            return -1
        
        return res if dfs(root)!=-1 else res+1