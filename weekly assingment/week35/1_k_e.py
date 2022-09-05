class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}
        for i,val in enumerate(nums):
            if val in rec: return [i,rec[val]]
            else: rec[target-val] = i
