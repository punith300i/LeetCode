func lengthOfLastWord(s string) int {
    var res int = 0
    for i:=len(s)-1; i>-1; i--{
        if s[i] != 32{
            res++
            if i-1 > -1 && s[i-1] == 32{
                break
            }
        }
    }
    return res
}