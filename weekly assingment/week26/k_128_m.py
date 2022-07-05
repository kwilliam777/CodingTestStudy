class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        nums=sorted(list(set(nums)))
        count = 1
        res = 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
                res = max(res,count)
            else:
                count=1
        return res
            
