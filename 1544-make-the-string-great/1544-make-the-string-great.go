func makeGood(s string) string {
    stack := []byte{}
    for i := 0; i < len(s); i++ {
        if len(stack) > 0 && abs(int(stack[len(stack) - 1]) - int(s[i])) == 32 {
            stack = stack[:len(stack) - 1]
        } else {
            stack = append(stack, s[i])
        }
    }
    return string(stack)
}

func abs(n int) int {
    if n > 0 { return n }
    return -n
}