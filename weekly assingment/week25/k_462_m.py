import statistics
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        val = int(statistics.median(nums))
        count = 0
        for i in nums:
            count += abs(i-val)
        return count
        
# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         nums.sort()
#         ans, median = 0, nums[len(nums) // 2]
#         for num in nums: ans += abs(median - num)
#         return ans
