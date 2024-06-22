func maxDistance(position []int, m int) int {
    
    //sort position list for Binary Search
    sort.Ints(position)
    
    l:=0
    r:=position[len(position)-1]-position[0]
    
    answer:= 0
    
    for l<=r{
        mid := l + (r-l)/2
        
        //check mag force
        cnt:=1
        last:=position[0]
        for i:=1;i<len(position);i++{
            if position[i] - last >= mid{
                cnt++
                last=position[i]
            }
        }
        
        // if we can place more balls i.e with cnt>m, we could place a larger magnitude force later
        // hence ignore the left half
        if cnt>=m{
            answer = mid
            l = mid+1
        }else{
            // ingore right half
            r = mid-1
        }
    }
    
    return answer
}