# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        while l1:
            n1+=str(l1.val)
            l1 = l1.next
        
        n2 = ""
        while l2:
            n2+=str(l2.val)
            l2 = l2.next
        
        l = None
        for i in str(int(n1)+int(n2))[::-1]:
            l1 = ListNode(int(i),None)
            l1.next = l
            l = l1
        return l
        