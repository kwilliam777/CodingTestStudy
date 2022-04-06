from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)
    
    
# def permute(self, nums):
#     return [[n] + p
#             for i, n in enumerate(nums)
#             for p in self.permute(nums[:i] + nums[i+1:])] or [[]]


# def permute(self, nums):
#     return nums and [p[:i] + [nums[0]] + p[i:]
#                      for p in self.permute(nums[1:])
#                      for i in range(len(nums))] or [[]]


# def permute(self, nums):
#     return reduce(lambda P, n: [p[:i] + [n] + p[i:]
#                                 for p in P for i in range(len(p)+1)],
#                   nums, [[]])
