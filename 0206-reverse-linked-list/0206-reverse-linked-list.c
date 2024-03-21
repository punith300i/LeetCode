/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var  prev, temp *ListNode
    var cur *ListNode = head
    for cur!=nil {
        temp = cur.Next
        cur.Next = prev
        prev = cur
        cur = temp
    }
    return prev
}