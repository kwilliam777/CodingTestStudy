from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = Counter(nums)
        result = [0]*(max(nums.keys())+1)

        for i in nums:
            result[i] = nums[i]*i
        print(result)
        
        ind = 0
        count = 0
        while ind < len(result)-1:
            if result[ind-1]+result[ind+1] <= result[ind]:
                count += result[ind]
            ind += 1
        
        return count
        
        
#         count = Counter(nums)
#         k = None
#         prev = curr = 0
        
#         for num in sorted(count):
#             earn = num * count[num]
            
#             if num - 1 == k:
#                 prev, curr = curr, max(prev + earn, curr)
#             else:
#                 prev, curr = curr, curr + earn
                
#             k = num
        
#         return curr
