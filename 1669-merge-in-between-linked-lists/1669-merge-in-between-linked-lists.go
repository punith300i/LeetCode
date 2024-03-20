/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
    var cur *ListNode = list1
    var cur2 *ListNode = list2
    var index int = 0
    var startNode *ListNode = nil
    var endNode *ListNode = nil
    
    for index!=b{
        if index+1 == a{
            startNode = cur
        }
        cur = cur.Next
        index++
    }
    endNode = cur.Next
    
    
    for cur2.Next!=nil{
        cur2 = cur2.Next
    }
    
    startNode.Next = list2
    cur2.Next = endNode
    
    return list1
    
}