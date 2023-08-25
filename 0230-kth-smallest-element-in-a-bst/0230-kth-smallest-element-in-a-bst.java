/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stk = new Stack<>();
        
        TreeNode cur = root;
        
        while(true){
            while(cur!=null){
                stk.push(cur);
                cur = cur.left;
            }
            TreeNode smallest = stk.pop();
            k-=1;
            if(k==0){
                return smallest.val;
            }
            cur = smallest.right;
        }
        
    }
}