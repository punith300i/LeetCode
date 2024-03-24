
func intersection(nums []int) int {
	slow, fast := 0, 0
	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast {
			return fast
		}
	}
}

func findDuplicate(nums []int) int {
	intersect := intersection(nums)

	start := 0
	for {
		start = nums[start]
		intersect = nums[intersect]
		if start == intersect {
			break
		}
	}
	return start
}