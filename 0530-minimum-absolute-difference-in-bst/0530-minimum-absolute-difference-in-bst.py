# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res=sys.maxsize
        self.prev=None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev:
                self.res=min(self.res,abs(node.val-self.prev.val))
            self.prev=node
            inorder(node.right)
        
        inorder(root)
        return self.res