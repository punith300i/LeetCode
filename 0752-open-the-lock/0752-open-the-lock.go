func openLock(deadends []string, target string) int {
    q := []string{"0000"}
    vis := map[string]struct{}{}
    for _, deadend := range deadends {
        vis[deadend] = struct{}{}
        if deadend == "0000" {
            return -1
        }
    }

    level := 0
    for len(q) > 0 {
        limit := len(q)
        for i := 0; i < limit; i++ {
            curr := q[0]
            q = q[1:]

            if curr == target {
                return level
            }

            nextLevel := generateLevel(curr)
            for _, next := range nextLevel {
                if _, ok := vis[next]; !ok {
                    vis[next] = struct{}{}
                    q = append(q, next)
                }
            }
        }
        level++
    }

    return -1
}

func generateLevel(s string) []string {
    nextLevel := []string{}
    for i := 0; i < 4; i++ {
        num := int(s[i] - '0')
        nextLevel = append(nextLevel, s[:i] + strconv.Itoa((num + 1) % 10) + s[i+1:]) 
        nextLevel = append(nextLevel, s[:i] + strconv.Itoa((num - 1 + 10) % 10) + s[i+1:]) 
    }

    return nextLevel
}