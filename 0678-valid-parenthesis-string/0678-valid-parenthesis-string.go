func checkValidString(s string) bool {
    l := 0
    notR := 0
    for _, v := range s {
        if v == '(' {
            l++
        } else {
            l--
        }
        if v != ')' {
            notR++
        } else {
            notR--
        }
        if notR < 0 { return false }
        l = max(0, l)
    }
    return l == 0
}

func max(a, b int) int {
    if a > b { return a }
    return b
}