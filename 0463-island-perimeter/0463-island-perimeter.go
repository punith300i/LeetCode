func islandPerimeter(grid [][]int) int {
    peri := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] == 1 {
                peri = dfs(&grid, i, j)
                break
            }
        }
    }
    return peri
}

func dfs(grid *[][]int, i int, j int) int {
    if i < 0 || i >= len(*grid) || j < 0 || j >= len((*grid)[0]) || (*grid)[i][j] == 0 {
        return 1
    }
    if (*grid)[i][j] == 2 {
        return 0
    }

    dy := []int{ 1, -1, 0, 0 }
    dx := []int{ 0, 0, 1, -1 }

    sum := 0
    (*grid)[i][j] = 2
    for k := 0; k < 4; k++ {
        y := i + dy[k]
        x := j + dx[k]
        sum += dfs(grid, y, x)
    }
    return sum
}