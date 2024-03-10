class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = Counter(nums1)
        result = []
        for element in nums2:
            if element not in result and element in hmap:
                result.append(element)
        return result