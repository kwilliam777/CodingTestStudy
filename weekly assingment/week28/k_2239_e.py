class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val = min([abs(i) for i in nums])
        return val if val in nums else -val
