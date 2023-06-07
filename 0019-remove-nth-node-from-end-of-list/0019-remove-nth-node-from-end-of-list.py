# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        temp = head
        length = 0
        while temp:
            temp = temp.next
            length+=1
        
        if length == n :
            return head.next

        index = length - n
        
        temp = head
        count = 0
        prev = head

        while temp and count!=index:
            prev = temp
            temp = temp.next
            count+=1
        
        prev.next = temp.next
        
        return head