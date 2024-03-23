func removeDuplicates(nums []int) int {
    var index int = 0
    for _, ele := range nums{
        if index<2 || ele!= nums[index-2] {
            nums[index]=ele
            index++
        }        
    }
    
    return index
}