class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iterate = k%len(nums)
        while iterate:
            nums.insert(0,nums.pop())
            iterate -= 1