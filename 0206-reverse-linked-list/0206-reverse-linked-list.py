# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        
        rev_head = None
        
        while head is not None:
            nxt_node = head.next
            head.next = rev_head
            rev_head = head
            head = nxt_node
        
        return rev_head