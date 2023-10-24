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
    public int preOrder(TreeNode root, int minimum, int maximum){
        if(root == null){
            return maximum - minimum;
        }
        maximum = Math.max(maximum, root.val);
        minimum = Math.min(minimum, root.val);
        
        return Math.max(preOrder(root.left, minimum, maximum), preOrder(root.right, minimum, maximum));
        
    }
    public int maxAncestorDiff(TreeNode root) {
        return preOrder(root,99999,-99999);
        
    }
}