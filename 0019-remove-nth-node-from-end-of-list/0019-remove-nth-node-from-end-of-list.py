# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size+=1
        
        if size == n:
            return head.next
        
        idx = size - n
        
        prev = head
        cur = head
        
        while cur and idx!=0:
            prev = cur
            cur = cur.next
            idx-=1
        
        prev.next = cur.next
        
        return head