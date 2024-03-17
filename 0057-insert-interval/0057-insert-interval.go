func insert(intervals [][]int, newInterval []int) [][]int {
    var result [][]int = [][]int{}
    for i := range intervals{
        if intervals[i][1] < newInterval[0]{
            result = append(result, intervals[i])
        }else if newInterval[1] < intervals[i][0]{
            result = append(result, newInterval)
            newInterval = intervals[i]
        }else if (intervals[i][1] >= newInterval[0]) || (intervals[i][0] <= newInterval[1]){
            if intervals[i][0] <  newInterval[0]{
                 newInterval[0] = intervals[i][0]
            }
            
            if intervals[i][1] > newInterval[1]{
                newInterval[1] = intervals[i][1]
            }
        }
    }
    result = append(result, newInterval)
    return result
}