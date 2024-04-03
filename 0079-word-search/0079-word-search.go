func exist(board [][]byte, word string) bool {
    dirs := [][]int{{0,-1}, {0,1}, {1,0}, {-1,0}}
    
    for i := range board{
        for j := range board[0]{
            if board[i][j] == word[0]{
                if findWord(0, &board, &dirs, i,j, word){
                    return true
                }
            }
        }
    }
    
    return false
}
func findWord(index int, b *[][]byte, d *[][]int, row int, col int, word string) bool {
    if index == len(word){
        return true
    }
        
    if row >= len(*b) || row < 0 || col >= len((*b)[0]) || col < 0 || (*b)[row][col]!= word[index] || (*b)[row][col] == 0{
        return false
    }
    
    // mark it as visitied
    lastVal := (*b)[row][col]
    (*b)[row][col] = 0
    
    for _, x := range *d{
        nrow := row+x[0]
        ncol := col+x[1]
        
        if findWord(index+1, b, d, nrow, ncol, word){
            return true
        }
    }
    
    // unmark as visited
    (*b)[row][col] = lastVal
    
    return false

}
    
    
    
    