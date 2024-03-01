func maximumOddBinaryNumber(s string) string {
    one := strings.Count(s, "1")
    zero := strings.Count(s, "0")
    res := strings.Repeat("1", one-1) + strings.Repeat("0", zero) + "1"
    return res
}