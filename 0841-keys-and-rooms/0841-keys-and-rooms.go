func canVisitAllRooms(rooms [][]int) bool {
    visited := map[int]bool{}
    dfs(0, visited, &rooms)
    return len(visited) == len(rooms)
    
}

func dfs(start int, visited map[int]bool, rooms *[][]int){
    visited[start] = true
    for _, key := range (*rooms)[start]{
        if _, ok := visited[key]; !ok{
            dfs(key,visited,rooms)
        }
    }
}