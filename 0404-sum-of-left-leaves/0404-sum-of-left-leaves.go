/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    res := 0
    return computeSum(root, false, &res)
}

func computeSum (root *TreeNode, isLeft bool, res *int) int {
    if root == nil{
        return 0
    }
    if root.Left == nil && root.Right == nil && isLeft == true{
        return root.Val
    }
    *res = computeSum(root.Left, true, res) + computeSum(root.Right, false, res)
    
    return *res
}
    
    