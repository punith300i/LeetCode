class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>(numCourses);
        
        for(int i=0; i<numCourses; i++){
            adj.add(new ArrayList<>());
        }
        
        for(int[] preq: prerequisites){
            adj.get(preq[1]).add(preq[0]);
            indegree[preq[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        
        for(int i=0; i<numCourses; i++){
            if(indegree[i]==0){
                queue.offer(i);
            }
        }
        
        int nodeVisited = 0;
        
        while (!queue.isEmpty()){
            int node = queue.poll();
            nodeVisited++;
            
            for(int nei:adj.get(node)){
                indegree[nei]--;
                if(indegree[nei]==0){
                    queue.offer(nei);
                }
            }
        }
        
        return nodeVisited == numCourses;
    }
}