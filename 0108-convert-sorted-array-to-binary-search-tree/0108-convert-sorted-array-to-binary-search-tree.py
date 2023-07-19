# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def binary_search(l, r):
            if l>r:
                return 
            if l<=r:
                mid = (l+r)//2
                node = TreeNode(nums[mid], None, None)
                node.left = binary_search(l,mid-1)
                node.right = binary_search(mid+1, r)
                return node
            
        return binary_search(0,len(nums)-1)