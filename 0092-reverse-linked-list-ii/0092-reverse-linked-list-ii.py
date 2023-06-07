# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or left == right:
            return head
        
        lefthead = head
        prev = head
        left_count = 1
        
        while left_count < left:
            prev = lefthead
            lefthead = lefthead.next
            left_count+=1
        
        
        no_of_revs = right-left
        revs = 0
        cur = lefthead
        n = cur.next
        
        while revs<no_of_revs and n!=None:
            cur.next = n.next
            n.next = lefthead
            lefthead = n
            n = cur.next
            
            revs+=1
        
        if left==1:
            return lefthead
        
        prev.next = lefthead
        
        return head