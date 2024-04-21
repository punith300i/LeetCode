type queue struct {
    elements []int
}

func (q *queue) enqueue(i int) {
    q.elements = append(q.elements, i)
}

func (q *queue) dequeue() int {
    if len(q.elements) == 0 {return -1}
    out := q.elements[0]
    q.elements = q.elements[1:]
    return out
}

func (q queue) len() int {
    return len(q.elements)
}

func NewQueue(n int) *queue {
    return &queue{
        elements: make([]int, 0, n),
    }
}

func validPath(n int, edges [][]int, source int, destination int) bool {
    edgeMap := make(map[int][]int)
    for i := range edges {
        n := edges[i][0]
        edgeMap[n] = append(edgeMap[n], edges[i][1])
        edgeMap[edges[i][1]] = append(edgeMap[edges[i][1]], edges[i][0])
    }
    
    visited := make(map[int]struct{})
    toVisit := NewQueue(n)

    toVisit.enqueue(source)

    for toVisit.len() > 0 {
        n := toVisit.dequeue()
        if n == destination {return true}
        if _, ok := visited[n]; ok {continue}
        visited[n] = struct{}{}
        for _, m := range edgeMap[n] {
            toVisit.enqueue(m)
        }
    }
    return false
}