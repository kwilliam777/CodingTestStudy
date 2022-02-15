from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        return [i for i in nums if nums[i] == 1][0]
    
    
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         res=0
#         for num in nums:
#             res = num ^ res
#         return res
