func tribonacci(n int) int {
    t0, t1, t2 := 0, 1, 1
    for n > 0 {
        t2, t1, t0 = t2 + t1 + t0, t2, t1
        n--;
    }
    return t0;
}