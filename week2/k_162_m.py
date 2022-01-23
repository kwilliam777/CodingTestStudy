class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ind = nums.index(max(nums))
        if ind == 0 or ind == len(nums)-1: return ind
        else:
            if nums[ind-1] < nums[ind] and nums[ind] > nums[ind+1]: return ind
            else: return None