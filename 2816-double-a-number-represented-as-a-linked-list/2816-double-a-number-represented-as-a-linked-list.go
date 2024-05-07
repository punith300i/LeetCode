func doubleIt(head *ListNode) *ListNode {
    c := compute(head)
    if c>0{
        return &ListNode{Val:c, Next:head} 
    }
    return head
}

func compute(n *ListNode) int {
    if n == nil{
        return 0
    }
    
    v := n.Val*2+compute(n.Next)
    n.Val = v%10
    
    return v/10
}