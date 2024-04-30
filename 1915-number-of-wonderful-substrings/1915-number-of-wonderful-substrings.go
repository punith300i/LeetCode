func wonderfulSubstrings(word string) int64 {
    count := 0
    bitmap := 0
	mapCount := make(map[int]int)
	mapCount[0]++
	n := len(word)

	for i := 0; i < n; i++ {
		ind := int(word[i]) - 97
		bitmap ^= 1 << ind

		count += mapCount[bitmap]

        diff := 1

		for j := 0; j < 10; j++ {
			diff = 1 << j
			count += mapCount[diff^bitmap]
		}

		mapCount[bitmap]++
	}
    return int64(count)
}