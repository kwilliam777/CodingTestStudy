from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = Counter(nums)
        result = 0
        val = 0
        for i in nums:
            if nums[i] > val:
                val = nums[i]
                result = i
        return result
    
# class Solution:
#     def majorityElement(self, nums):
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key=counts.get)
