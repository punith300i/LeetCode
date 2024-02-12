# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root,lst):
            nonlocal res
            
            if root is None:
                return
            
            if root.left == None and root.right==None:
                res.append("->".join(map(str,lst.copy() + [root.val])))
                return
            
            # left
            lst.append(root.val)
            dfs(root.left,lst)
            lst.pop()
            
            # right
            lst.append(root.val)
            dfs(root.right,lst)
            lst.pop()
            
        dfs(root,[])
        return res