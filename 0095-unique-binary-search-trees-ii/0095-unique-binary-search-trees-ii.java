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
    public List<TreeNode> generateTrees(int n) {
        return helper(1,n);
    }
    
    List<TreeNode> helper(int first, int last){
        
        List<TreeNode> list = new ArrayList();
        
        if( first > last ){
            list.add(null);
            return list;
        }
        
        if (first == last ){
            list.add(new TreeNode(first));
            return list;
        }
        
        for(int root=first; root<=last; root++){
            List<TreeNode> leftTrees = helper(first, root-1);
            List<TreeNode> rightTrees = helper(root+1, last);
            
            for (TreeNode lnode : leftTrees){
                for( TreeNode rnode: rightTrees){
                    TreeNode node = new TreeNode(root, lnode, rnode);
                    list.add(node);
                }
            }
        }
        
        return list;
        
    }
}