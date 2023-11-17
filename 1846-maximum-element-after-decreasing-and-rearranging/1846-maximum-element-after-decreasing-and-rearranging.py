class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        max_element = 1
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] >= 2:
                max_element = arr[i-1]+1
                arr[i] = max_element
            else:
                max_element = arr[i]
        return max_element