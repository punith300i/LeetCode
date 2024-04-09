func timeRequiredToBuy(tickets []int, k int) int {
    queue := make([]int, 0)
    counts := 0
    
    for i := range tickets{
        queue = append(queue, i)
    }
    
    
    for len(queue)>0 {
        idx := queue[0]
        queue = queue[1:]
        
        tickets[idx]--
        counts++
        
        if tickets[idx] == 0 && idx == k {
            return counts
        }
        
        if tickets[idx] > 0{
            queue = append(queue, idx)
        }
        
    }
    return counts
}