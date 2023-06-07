# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        current_node = head
        next_node = current_node.next
        
        while(next_node!=None):
            current_node.next = next_node.next
            next_node.next = head
            head = next_node
            next_node = current_node.next
        
        return head