class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        for i in range(len(num)):
            t = target - num[i]
            if t in num[i+1:]:
                return [i+1,i+1+num[i+1:].index(t)+1]
                
                
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l, r = 0, len(numbers) - 1
#         while l < r:
#             sum = numbers[l] + numbers[r]
#             if sum == target:
#                 return [l + 1, r + 1]
#             elif sum > target:
#                 r -= 1
#             else:
#                 l += 1
