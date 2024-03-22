/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverse(head *ListNode) *ListNode{
    var prev, next * ListNode
    cur := head
    for cur!=nil{
        next = cur.Next
        cur.Next = prev
        prev = cur
        cur = next
    }
    return prev
}

func isPalindrome(head *ListNode) bool {
    fast := head
    slow := head
    cur := head
    
    for fast!=nil && fast.Next!=nil{
        slow = slow.Next
        fast = fast.Next.Next
    }
    
    slow = reverse(slow)
    
    for slow!=nil {
        if cur.Val != slow.Val{
            return false
        }
        cur = cur.Next
        slow = slow.Next
    }
    
    return true
}