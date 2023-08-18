class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        int[] degree = new int[n];
        int[][] adj = new int[n][n];
        
        for(int[] road: roads){
            degree[road[0]]++;
            degree[road[1]]++;
            adj[road[0]][road[1]]=1;
            adj[road[1]][road[0]]=1;
        }
        
        int rank = 0;
        
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                rank = Math.max(rank, degree[i] + degree[j] - adj[i][j]);
            }
        }
        return rank;
    }
}