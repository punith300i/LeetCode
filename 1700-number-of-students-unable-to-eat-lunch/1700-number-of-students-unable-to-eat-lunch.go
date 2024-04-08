func rotateLeft(s []int) []int {
    temp := s[0]
    for i:=0; i < len(s) - 1; i++ {
        s[i] = s[i+1]
    }
    s[len(s)-1] = temp
    return s
}

func removeEle(s []int, ele int) []int {
    return append(s[:ele], s[ele+1:]...)
}

func countStudents(students []int, sandwiches []int) int {
    var idx int
    for len(students) > 0 && len(sandwiches) > 0 {
        if students[0] == sandwiches[0] {
            students = removeEle(students, 0)
            sandwiches = removeEle(sandwiches, 0)
            idx = 0
        } else {
            students = rotateLeft(students)
            idx++
        }
        if idx > len(students) {
            break
        }
    }
    return len(students)
}