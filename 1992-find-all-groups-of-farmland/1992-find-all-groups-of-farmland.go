func findFarmland(land [][]int) [][]int {
    result := make([][]int,0)
    
    for i, r := range land {
        for j, _ := range r {
            if land[i][j] == 1 {
                
                bottomRow, bottomCol := 0,0
                dfs(land, i, j, &bottomRow, &bottomCol)
                result = append(result, []int{i,j,bottomRow, bottomCol})
            }
        }
    }

    return result
}

func dfs(land [][]int, r, c int, bottomRow, bottomCol *int) {
    if r < 0 || r >= len(land) || c < 0 || c >= len(land[r]) || land[r][c] == 0  {
        return 
    }

    land[r][c] = 0

    *bottomRow = max(r, *bottomRow)
    *bottomCol = max(c, *bottomCol)

    dfs(land, r+1, c, bottomRow, bottomCol)
    dfs(land, r, c+1, bottomRow, bottomCol)
}