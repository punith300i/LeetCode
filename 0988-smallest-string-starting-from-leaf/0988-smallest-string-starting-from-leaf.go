/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type Pair struct {
	Node *TreeNode
	Cur  string
}

func smallestFromLeaf(root *TreeNode) string {
	res := "{"
	q := []Pair{{root, ""}}
	for len(q) > 0 {
		node, cur := q[0].Node, q[0].Cur
        q = q[1:]
		cur = string(rune(int('a')+node.Val)) + cur
		if node.Left == nil && node.Right == nil {
			res = min(res, cur)
		}
		if node.Left != nil {
			q = append(q, Pair{node.Left, cur})
		}
		if node.Right != nil {
			q = append(q, Pair{node.Right, cur})
		}
	}
	return res
}
