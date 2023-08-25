# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def solve(root, parent):
            
            if root is None:
                return 0
            
            res = 1 if root.val>=parent else 0
            parent = max(parent, root.val)
            
            res+=solve(root.left, parent)
            res+=solve(root.right, parent)
            
            return res
            
        return solve(root, root.val)