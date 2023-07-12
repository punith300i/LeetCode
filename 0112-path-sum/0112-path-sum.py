# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(root,cur_sum, target_sum):
            if root is None:
                return False
            if root.left is None and root.right is None and cur_sum+root.val == target_sum:
                return True
            return dfs(root.left,cur_sum+root.val, target_sum) or dfs(root.right, cur_sum+root.val, target_sum)
            
        
        return dfs(root,0,targetSum)