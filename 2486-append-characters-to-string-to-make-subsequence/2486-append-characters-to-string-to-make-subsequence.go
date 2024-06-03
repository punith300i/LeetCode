func appendCharacters(s string, t string) int {
    sI:=0
    tI:=0
    for sI<len(s) && tI<len(t) {
        if s[sI]==t[tI] {
            sI++
            tI++
        } else {
            sI++
        }
    }
    
    return len(t)-(tI)
}