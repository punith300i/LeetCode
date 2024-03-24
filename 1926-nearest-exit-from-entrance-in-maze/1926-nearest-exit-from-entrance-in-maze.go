func nearestExit(maze [][]byte, entrance []int) int {
    directions := [][2]int{{-1,0},{1,0}, {0,1}, {0,-1}}
    queue := make([][2]int,0,len(maze))
    queue = append(queue, [2]int{entrance[0], entrance[1]})
    
    maze[entrance[0]][entrance[1]] = '+'
    
    var result int = 0
    
    for len(queue) > 0{
        result++
        size := len(queue)
        
        for i:=0; i<size ;i++{
            row, col := queue[0][0], queue[0][1]
            queue = queue[1:]
            
            for _, coord := range directions{
                nRow := row + coord[0]
                nCol := col + coord[1]
                if isOut(nRow, nCol, maze) || maze[nRow][nCol]=='+'{
                    continue
                }
                if isExit(nRow, nCol, maze){
                    return result
                }
                maze[nRow][nCol]='+'
                queue = append(queue, [2]int{nRow,nCol})
                
            }
            
        }
        
    }
    
    return -1
}

func isExit(row int, col int, maze [][]byte) bool {
    return row == 0 || col == 0 || row == len(maze)-1 || col == len(maze[row])-1
}

func isOut(row int, col int, maze [][]byte) bool {
    return row<0 || col<0 || row >= len(maze) || col >= len(maze[row])
}