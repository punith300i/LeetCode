import (
    "sort"
    "strconv"
)

func findRelativeRanks(score []int) []string {
    dic, rank, answer := make(map[int]string), make([]int, len(score)), make([]string, len(score))
    
    copy(rank, score)
    
    sort.Sort(sort.Reverse(sort.IntSlice(rank)))
    
    dic[rank[0]] = "Gold Medal"
    
    if len(rank) > 1 {
        dic[rank[1]] = "Silver Medal"
    }
    
    if len(rank) > 2 {
        dic[rank[2]] = "Bronze Medal"
    }
    
    for i := 3; i < len(rank); i++ {
        dic[rank[i]] = strconv.Itoa(i + 1)
    }
    
    for k, v := range score {
        answer[k] = dic[v]
    }
    
    return answer
}