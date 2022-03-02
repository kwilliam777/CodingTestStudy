class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        ind = len(nums)//2
        if len(nums)%2==0: return (nums[ind-1]+nums[ind])/2
        else: return nums[ind]/1
