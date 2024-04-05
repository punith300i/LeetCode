type SeatManager struct {
    UnReserve *MinHeap
}


func Constructor(n int) SeatManager {
    data := &MinHeap{}
    for i:=1; i<n+1; i++{
        *data = append(*data, i)
    }
    heap.Init(data)
    return SeatManager{UnReserve: data}
}


func (this *SeatManager) Reserve() int {
    return heap.Pop(this.UnReserve).(int)
}   


func (this *SeatManager) Unreserve(seatNumber int)  {
    heap.Push(this.UnReserve, seatNumber)
}

// defining heap interface

type MinHeap []int

func (h MinHeap) Len() int{
    return len(h)
}

func (h MinHeap) Less(i, j int) bool {
    return h[i] < h[j]
}

func (h MinHeap) Swap(i,j int) {
    h[i],h[j] = h[j],h[i]
}

func (h *MinHeap) Push(x any) {
    *h = append(*h, x.(int))
}

func (h *MinHeap) Pop() any{
    old := *h
	n := len(old)
	x := old[n-1]
    *h = old[0:n-1]
	return x
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */