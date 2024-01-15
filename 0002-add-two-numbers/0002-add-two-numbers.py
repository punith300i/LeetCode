# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        cur = result
        while l1 and l2 :
            sum_val = l1.val + l2.val + carry
            carry = sum_val//10
            temp = ListNode(sum_val%10)
            cur.next = temp
            cur=temp 
            if carry and l2.next is None and l1.next is None:
                temp = ListNode(carry%10)
                cur.next = temp
                cur=temp
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum_val = l1.val + carry
            carry = sum_val//10
            temp = ListNode(sum_val%10)
            cur.next = temp
            cur=temp
            if carry and l1.next is None:
                temp = ListNode(carry%10)
                cur.next = temp
                cur=temp
            l1 = l1.next
        
        while l2:
            sum_val = l2.val + carry
            carry = sum_val//10
            temp = ListNode(sum_val%10)
            cur.next = temp
            cur=temp
            if carry and l2.next is None:
                temp = ListNode(carry%10)
                cur.next = temp
                cur=temp
            l2 = l2.next
        
        
        return result.next