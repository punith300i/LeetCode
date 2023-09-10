class Solution {
    
    int[] parent;
    
    public int find(int node){
        while(node != parent[node]){
            node = parent[node];
        }
        return node;
    }
    
    public void union(int i, int j){
        int pi = find(i);
        int pj = find(j);
        parent[pj] = pi;
    }
    
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        parent = new int[n+1];
        
        for(int i=0; i<parent.length; i++){
            parent[i] = i;
        }
        
        for(int[] edge: edges){
            if(find(edge[0]) == find(edge[1])){
                return edge;
            }else{
                union(edge[0],edge[1]);
            }
        }
        return edges[0];
    }
}