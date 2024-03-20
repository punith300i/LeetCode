# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        index = 0
        while index!=b:
            if index+1 == a:
                start_node = cur
            cur = cur.next
            index+=1
        end_node = cur.next
        
        cur = list2
        while cur.next!=None:
            cur = cur.next
        
        start_node.next = list2
        cur.next = end_node
        
        return list1