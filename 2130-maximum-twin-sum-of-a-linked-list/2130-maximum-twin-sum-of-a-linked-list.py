# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        cur = head
        result = float('-inf')
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        for i in range(len(stack)//2):
            result = max(result, (cur.val + stack.pop()))
            cur = cur.next
        return result
            