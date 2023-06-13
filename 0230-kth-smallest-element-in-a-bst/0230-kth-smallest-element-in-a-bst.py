# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = collections.deque()
        
        cur = root
        while True:
            while cur is not None:
                s.append(cur)
                cur=cur.left
            smallest = s.pop()
            k-=1
            if k==0:
                return smallest.val
            cur = smallest.right
        
        return 0