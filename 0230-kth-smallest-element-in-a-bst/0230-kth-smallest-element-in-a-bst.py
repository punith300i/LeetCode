# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while(True):
            while(cur is not None):
                stack.append(cur)
                cur = cur.left
            k-=1
            min_val = stack.pop()
            if k==0:
                return min_val.val
            cur = min_val.right
        
        return -1