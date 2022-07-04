class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[i+1:])==sum(nums[:i]):
                return i
        return -1
    
    
#     def findMiddleIndex(self, nums: List[int]) -> int:               
#         leftSum = 0
#         rightSum = sum(nums)

#         for i in range(len(nums)):
#             if leftSum == rightSum - nums[i]:
#                 return i

#             leftSum += nums[i]
#             rightSum -= nums[i]

#         return -1
