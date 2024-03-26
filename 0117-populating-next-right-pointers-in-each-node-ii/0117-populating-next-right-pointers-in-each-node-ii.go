/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
	
    if root == nil{
        return root
    }
    
    var queue []*Node = []*Node{}
    queue = append(queue, root)
    
    for len(queue)>0{
        size := len(queue)
        // add nodes to queue
        for i:=0 ;i<size;i++{
            node := queue[0]
            queue = queue[1:]
            
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil{
                queue = append(queue, node.Right)
            }
        }
        // connect nodes
        for i:=1; i<len(queue);i++{
            queue[i-1].Next = queue[i]
        }
    }
    
    return root
}