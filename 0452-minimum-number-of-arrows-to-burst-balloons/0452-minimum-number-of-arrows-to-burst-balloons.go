func findMinArrowShots(points [][]int) int {
    var minArrows int = 1
    sort.Slice(points, func(i int, j int) bool{
            return points[i][1] < points[j][1]
        })
    // var that stores last point that is still in range
    prev := points[0]
    for i := 1; i < len(points); i++{
        if points[i][0] <= prev[1] && prev[1] <= points[i][1]{
            continue
        }else{
            minArrows++
            prev=points[i]
        }
    }
    return minArrows
}