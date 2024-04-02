func isIsomorphic(s string, t string) bool {
    hmap1 := map[byte]byte{}
    hmap2 := map[byte]byte{}
    
    for i := range s {
        _, ok1 := hmap1[s[i]]
        _, ok2 := hmap2[t[i]]
        
        if !ok1 && !ok2 {
            hmap1[s[i]] = t[i]
            hmap2[t[i]] = s[i]
        }else if hmap1[s[i]]!=t[i] || hmap2[t[i]]!=s[i]{
            return false
        } 
    }
    
    return true
}