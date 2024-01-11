# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], min_value: int, max_value: int) -> int:
        if root is None:
            return max_value - min_value
        
        min_value = min(min_value, root.val)
        max_value = max(max_value, root.val)
        
        return max(self.traverse(root.left, min_value, max_value), 
                   self.traverse(root.right, min_value, max_value))
                   
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 99999, -99999)
        