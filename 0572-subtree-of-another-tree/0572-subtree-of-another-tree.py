# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        flags = []
        def is_same(r,s):
            if r is None and s is None:
                return True
            if r is None or s is None:
                return False
            
            return r.val == s.val and is_same(r.left, s.left) and is_same(r.right, s.right)
        
        def pre_order(r,s):
            if r is None:
                return 
            if r.val == s.val:
                flags.append(is_same(r,s))

            pre_order(r.left,s)
            pre_order(r.right,s)
        
        
        pre_order(root,subRoot)
        return any(flags)
            