# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_map = dict()
        
        dhead = ListNode(0,head)
        
        cur = dhead
        prefix_sum = 0
        while cur:
            prefix_sum+=cur.val
            prefix_map[prefix_sum] = cur
            cur = cur.next
        
        cur = dhead
        prefix_sum = 0
        while cur:
            prefix_sum+=cur.val
            cur.next = prefix_map[prefix_sum].next
            cur = cur.next
        
        return dhead.next