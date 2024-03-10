class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = Counter(nums1)
        result = []
        for element in nums2:
            if element in hmap and element not in result:
                result.append(element)
        return result