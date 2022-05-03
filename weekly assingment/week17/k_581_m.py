class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        ind = [-1,-1]
        for i in range(len(nums)):
            if nums[i]!=nums2[i]:
                ind[0]=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=nums2[i]:
                ind[1]=i
                break
            
        return ind[1]-ind[0]+1 if -1 not in ind else 0
