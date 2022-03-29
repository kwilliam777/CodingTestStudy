class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-1,m-1,-1):
            nums1.pop(i)
        nums1.extend(nums2)
        nums1.sort()
