class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                zeros.append(nums.pop(i))
        nums.extend(zeros)
