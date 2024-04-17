func sortColors(nums []int)  {
    freq := make(map[int]int)
    
    for i := range nums{
        freq[nums[i]]++
    }
    
    i:=0
    j:=0
    for i<3 {
        if freq[i] > 0{
            nums[j]=i
            freq[i]--
            j++
        }else{
            i++
        }
    }
    
}