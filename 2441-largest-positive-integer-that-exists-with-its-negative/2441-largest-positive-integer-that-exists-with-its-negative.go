func findMaxK(nums []int) int {
    numsMap := make(map[int]bool)
    for _, val := range(nums){
        if _, ok := numsMap[val]; !ok{
            numsMap[val]=true
        }
    }
    
    sort.Slice(nums, func (i,j int) bool {
        return nums[i] > nums[j]
    })    
    
    for i:=len(nums)-1; i>=0; i--{
        if numsMap[-nums[i]]{
            return -nums[i]
        }
    }
    return -1
}