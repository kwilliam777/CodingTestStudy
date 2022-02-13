class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        checker=[]
        
        for index in range(len(nums)-1,-1,-1):
            if nums[index] in checker :
                nums.pop(index)
            else :
                checker.append(nums[index])
        
