# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        
        last_node = None
        cur, main_cur = head, head
        
        while main_cur.next.next:
            cur = main_cur
            while cur.next:
                last = cur
                cur = cur.next
            last.next = None
            nxt_node = main_cur.next
            main_cur.next = cur
            cur.next = nxt_node
            main_cur = nxt_node
            if not main_cur.next:
                break
        return head