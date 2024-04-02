/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import(
    "slices";
)
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder)==0 || len(inorder)==0 {
        return nil
    }
    
    var root *TreeNode = &TreeNode{ 
                    Val:preorder[0],
                    Left: nil,
                    Right: nil,
             }
    var pivot int = slices.Index(inorder, preorder[0])
    
    root.Left = buildTree(preorder[1:pivot+1], inorder[:pivot])
    root.Right = buildTree(preorder[pivot+1:], inorder[pivot+1:])
    
    return root
}