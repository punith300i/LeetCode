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
import java.util.ArrayList;
class Solution {
    public static void inorder(TreeNode root, ArrayList<Integer> list){
        if(root == null){
            return;
        }
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
        
    }
    
    public static TreeNode findBalancedRoot( ArrayList<Integer> list, int low, int high){
        if (low > high){
            return null;
        }
        int mid = low + (high-low)/2;
        TreeNode root = new TreeNode(list.get(mid));
        root.left = findBalancedRoot(list, low, mid-1);
        root.right = findBalancedRoot(list, mid+1, high);
        return root;
    }
    
    public TreeNode balanceBST(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<>();
        if(root == null){
            return root;
        }
        
        inorder(root, list);
        
        return findBalancedRoot(list, 0, list.size()-1);
        
    }
}