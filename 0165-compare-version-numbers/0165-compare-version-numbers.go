func compareVersion(version1 string, version2 string) int {
    v1s := strings.Split(version1, ".")
    v2s := strings.Split(version2, ".")
    length := len(v1s)
    if len(v2s) > length {
        length = len(v2s)
    }
    v1i := make([]int, length)
    v2i := make([]int, length)
    for i, v := range v1s {
        iv, _ := strconv.Atoi(v)
        v1i[i] = iv
    }
    for i, v := range v2s {
        iv, _ := strconv.Atoi(v)
        v2i[i] = iv
    }
    for i := 0; i < length; i++ {
        if v1i[i] < v2i[i] {
            return -1
        } else if v1i[i] > v2i[i] {
            return 1
        }
    }
    return 0
}