from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = Counter([i for i in nums if i < k])
        ans = 0
        for i in nums:
            if k-i in nums and nums[i]>0 and nums[k-i]>0:
                count = nums[i]//2 if i==k-i else min(nums[i],nums[k-i])
                nums[i]-=count
                nums[k-i]-=count
                ans+=count
        return ans
    
    
# from collections import defaultdict
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         pair = defaultdict(int) # integer 0 is the default value of all the keys
#         res = 0
        
#         for n in nums:
#             if pair[n]: # if we encountered k - n already
#                 res += 1
#                 pair[n] -= 1
#             else: # if we did'n find a pair yet
#                 pair[k - n] += 1
                
#         return res
