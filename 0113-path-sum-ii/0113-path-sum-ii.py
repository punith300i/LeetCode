# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []
        def dfs(root, cur_sum, target_sum,ls):
            if root is None:
                return 
            
            
            
            if root.left is None and root.right is None and cur_sum + root.val == target_sum:
                self.res.append(ls+[root.val])
            
            dfs(root.left, cur_sum + root.val, target_sum, ls+[root.val])
            dfs(root.right, cur_sum + root.val, target_sum, ls+[root.val])
            
        
        dfs(root,0, targetSum, [])
        
        return self.res