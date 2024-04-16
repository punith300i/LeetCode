/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    if root == nil {
        return root
    }
    if depth == 1 {
        return &TreeNode{val,root,nil}
    }
    if depth == 2 {
        l, r := root.Left, root.Right
        root.Left, root.Right = &TreeNode{val,l,nil}, &TreeNode{val,nil,r}
    } else {
        addOneRow(root.Left, val, depth-1)
        addOneRow(root.Right, val, depth-1)
    }
    return root
}