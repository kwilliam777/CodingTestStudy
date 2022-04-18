class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        ans.append([nums[i],nums[j],nums[k]])
        return ans

    
# class Solution:
#     def threeSum(self, nums):
#         res = []
#         nums.sort()
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             l, r = i+1, len(nums)-1
#             while l < r:
#                 s = nums[i] + nums[l] + nums[r]
#                 if s < 0:
#                     l +=1 
#                 elif s > 0:
#                     r -= 1
#                 else:
#                     res.append((nums[i], nums[l], nums[r]))
#                     while l < r and nums[l] == nums[l+1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r-1]:
#                         r -= 1
#                     l += 1; r -= 1
#         return res 
    
    
# class Solution(object):
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3: return []
#         nums.sort()
#         res = set()
#         for i, v in enumerate(nums[:-2]):
#             if i >= 1 and v == nums[i-1]:
#                 continue
#             d = {}
#             for x in nums[i+1:]:
#                 if x not in d:
#                     d[-v-x] = 1
#                 else:
#                     res.add((v, -v-x, x))
#         return map(list, res)
