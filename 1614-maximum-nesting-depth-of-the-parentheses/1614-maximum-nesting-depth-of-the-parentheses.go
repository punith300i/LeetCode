func maxDepth(s string) int {
    stack := []string{}

	maxDepth := 0
	for _, char := range s {
		temp := string(char)

		if temp == "(" {
            // push
            stack = append(stack, string(temp))
		} else if temp == ")" {
			// pop
            stack = stack[:len(stack)-1]
		}

		maxDepth = max(maxDepth, len(stack))
	}

	return maxDepth
}