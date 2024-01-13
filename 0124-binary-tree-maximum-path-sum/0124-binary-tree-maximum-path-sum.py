# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_val = -99999
        def dfs(root: Optional[TreeNode]) -> int:
            
            nonlocal max_val
            if root is None:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            
            max_val = max(max_val, root.val + left + right)
            
            return root.val + max(left, right)
        
        dfs(root)
        return max_val