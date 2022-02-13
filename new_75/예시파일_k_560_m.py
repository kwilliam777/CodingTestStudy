class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		ans,prefsum,d=0,0,{0:1}

		for num in nums:
			prefsum = prefsum + num

			if prefsum-k in d: ans = ans + d[prefsum-k]

			if prefsum not in d: d[prefsum] = 1
			else: d[prefsum] = d[prefsum]+1

		return ans
#         def keepadd(ind,temp):
#             if ind +1 == len(nums) or temp > k:
#                 return
#             elif temp == k:
#                 self.count += 1
#             elif temp < k:
#                 temp += nums[ind]
#                 keepadd(ind+1,temp)
        
#         self.count = 0
#         for i in range(len(nums)):
#             temp = 0
#             keepadd(i,temp)
        
#         return self.count
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         temp = sum(nums[i:j+1])
        #         if temp == k:
        #             count += 1
        #         elif temp > k:
        #             break
        # return count