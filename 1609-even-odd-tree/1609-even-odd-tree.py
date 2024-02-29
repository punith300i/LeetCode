# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            if level%2==0:
                for i in queue:
                    if i.val%2==0:
                        return False
                for i in range(1,len(queue)):
                    if queue[i-1].val>=queue[i].val:
                        return False
            else:
                for i in queue:
                    if i.val%2==1:
                        return False
                for i in range(1,len(queue)):
                    if queue[i-1].val<=queue[i].val:
                        return False
            
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            level+=1
            
        return True