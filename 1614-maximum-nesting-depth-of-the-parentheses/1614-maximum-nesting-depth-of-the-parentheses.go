func maxDepth(s string) int {   
    counter := 0
	maxDepth := 0
	for _, char := range s {
		temp := string(char)
		if temp == "(" {
            counter++
		} else if temp == ")" {
            counter--
		}
		maxDepth = max(maxDepth, counter)
	}
	return maxDepth
}