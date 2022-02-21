class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        print(len(nums))
        posind = []
        for i in range(len(nums)):
            if nums[i]>0:
                posind.append(i)
        sums = []
        for i in range(len(posind)):
            for j in range(i+1,len(posind)):
                sums.append(sum(nums[posind[i]:posind[j]+1]))
        return max(sums)

# class Solution:
# 	def maxSubArray(self, nums: List[int]) -> int:
# 		max_sum = nums[0]
# 		current_sum = 0

# 		for num in nums:
# 			current_sum = current_sum + num
# 			max_sum = max(max_sum , current_sum)

# 			if current_sum < 0:
# 				current_sum = 0

# 		return max_sum
