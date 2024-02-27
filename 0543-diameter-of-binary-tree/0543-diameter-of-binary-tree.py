# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def find_diameter(root):
            nonlocal res
            
            if root is None:
                return 0
            
            l = find_diameter(root.left)
            r = find_diameter(root.right)
            
            res = max(res, 1+l+r)
            
            return 1+max(l,r)
        
        find_diameter(root)
        return res-1