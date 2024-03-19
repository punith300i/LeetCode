func leastInterval(tasks []byte, n int) int {
    // compute frequency array
    freq := make([]int, 26)
    for _, task := range tasks{
        freq[task -'A']++
    }
    
    // sort frequencies
    sort.Ints(freq)
    
    // most frequent task
    max_freq := freq[len(freq)-1]
    
    // no of idle slots = no of most freq task - 1 (as we dont have idle states in the end) * n
    idle_slots := (max_freq - 1) * n
    
    // fill the idle slots with remaining available tasks
    for i:=len(freq)-2;i>=0 && idle_slots>0;i--{
        idle_slots -= min_val(freq[i], max_freq-1)
    }
    
    // if there are idle slots present then add it to the final result
    if idle_slots>0{
        return len(tasks) + idle_slots
    }else{
        return len(tasks)
    }
}


// helper function to compute min value
func min_val(i,j int) int{
    if i<=j{
        return i
    }else{
        return j
    }
}