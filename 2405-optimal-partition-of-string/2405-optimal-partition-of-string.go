func partitionString(s string) int {
    hmap := map[byte]bool{}
    ans := 1
    for i:=0; i<len(s); i++{
        if hmap[s[i]]{
            ans++
            hmap = map[byte]bool{}
        }
        hmap[s[i]] = true
    }
    return ans
}