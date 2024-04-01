func lengthOfLastWord(s string) int {
    var res int = 0
    for i:=len(s)-1; i>-1; i--{
        if string(s[i])!= " "{
            res++
            if i-1 > -1 && string(s[i-1]) == " "{
                break
            }
        }
    }
    return res
}