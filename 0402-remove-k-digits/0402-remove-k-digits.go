func removeKdigits(num string, k int) string {
    length := len(num)
    if length == k {
        return "0"
    }
    
    stack := make([]byte, 0)
    // push sentinel
    stack = append(stack, '0'-1)
    
    // process num
    for i := 0; i < length; {
        if k == 0 {
            // append remain and goto next step
            stack = append(stack, num[i:]...)
            break
        }
        
        if num[i] >= stack[len(stack)-1] {
            stack = append(stack, num[i])
            i++
        } else {
            stack = stack[:len(stack)-1]
            k--
        }
    }
    
    // remove sentinel from head
    // remove k elems form tail
    stack = stack[1:len(stack)-k]
    
    // remove prefix zero
    nozeroIndex := 0
    for ; nozeroIndex < len(stack)-1; nozeroIndex++ {
        // compare with '0', not 0
        if stack[nozeroIndex] != '0' {
            break
        }
    }
    stack = stack[nozeroIndex:]
    
    return string(stack)
}