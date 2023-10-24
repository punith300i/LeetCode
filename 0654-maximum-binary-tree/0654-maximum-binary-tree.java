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
    public static TreeNode construct(int[] nums, int left, int right){
        if(left > right){
            return null;
        }
        int pivot = left;
        for (int i = pivot+1; i<=right; i++){
            if(nums[i] >= nums[pivot]){
                pivot = i;
            }
        }
        TreeNode root = new TreeNode(nums[pivot]);
        root.left = construct(nums, left, pivot-1);
        root.right = construct(nums, pivot+1, right);
        return root;
    }
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums, 0, nums.length - 1);
    }
}