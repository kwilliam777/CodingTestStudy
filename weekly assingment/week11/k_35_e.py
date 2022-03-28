class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for n in [nums.index(i) for i in sorted(nums, key = lambda x:abs(x-target))]:
            if nums[n]-target>=0:
                return n
        return len(nums)
    
    
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         start = 0
#         end = len(nums)-1
#         res = 0
#         while start <= end:
#             mid = start + (end-start)//2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 res = mid + 1
#                 start = mid + 1
#             else:
#                 end = mid - 1
                
#         return res
