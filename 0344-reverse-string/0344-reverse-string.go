func reverseString(s []byte)  {
    var l int = 0
    var r int = len(s)-1
    for l<r{
        s[l],s[r] = s[r],s[l]
        l++
        r--
    }
}