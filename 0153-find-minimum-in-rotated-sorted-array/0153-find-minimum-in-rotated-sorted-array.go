func findMin(nums []int) int {
	left := 0
	right := len(nums) - 1

	for left < right {
		mid := (left + right) / 2

		if nums[mid] > nums[len(nums)-1] {
			left++
		} else {
			right--
		}
	}

	return nums[left]
}