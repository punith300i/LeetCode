/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumNumbers(root *TreeNode) int {
    totalSum := 0
    var helper func(*TreeNode, int) // nested function must be declared first if you're doing recursion
    
    helper = func(node *TreeNode, sum int) {
        if node == nil { return }
        
        sum = (sum * 10) + node.Val
        if node.Left == nil && node.Right == nil {
            totalSum += sum
            return
        }
        helper(node.Left, sum)
        helper(node.Right, sum)
    }
    helper(root, 0)
    
    return totalSum
}