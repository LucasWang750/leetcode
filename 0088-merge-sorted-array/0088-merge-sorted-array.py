class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        for i in range(m + n):
            if index > n - 1:
                break
            if nums2[index] < nums1[i] or i >= m + index:
                nums1.insert(i, nums2[index])
                del nums1[-1]
                index += 1
            
        