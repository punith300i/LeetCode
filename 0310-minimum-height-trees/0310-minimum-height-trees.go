func findMinHeightTrees(n int, edges [][]int) []int {
    var graph = map[int][]int{}
    var indegree = map[int]int{}
    
    if len(edges)==0{
        return []int{0}
    }
    
    // create graph
    for _, edge := range edges {
        graph[edge[0]] = append(graph[edge[0]], edge[1])
        graph[edge[1]] = append(graph[edge[1]], edge[0])
        indegree[edge[0]]++
        indegree[edge[1]]++
    }
    
    // bfs through all leaves as starting point
    queue := []int{}
    result := []int{}
    
    
    // add all the leaves to the queue i.e. the ones with indegree with value = 1
    for node, indeg := range indegree{
        if indeg == 1{
            queue = append(queue, node)
        }
    }
    
    
    // Run bfs until a node with indegree is left i.e. until we reach a centroid node.
    
    for len(queue)>0{
        size := len(queue)
        // update result to null until we interate to he last node with indegree = 1 which will be the centroid.
        result = []int{}
        for i:=0; i<size ;i++{
            node := queue[0]
            queue = queue[1:]
            result = append(result, node)
            for _, adjNode := range graph[node]{
                    indegree[adjNode]--
                    if indegree[adjNode] == 1{
                        queue = append(queue, adjNode)
                }

            }
        }
        
       
    }
    
    return result
}