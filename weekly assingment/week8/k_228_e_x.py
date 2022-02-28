class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0: return result
        elif len(nums) == 1: 
            result.append(str(nums[0]))
            return result
        elif len(nums) == 2:
            if nums[1] - nums[0] != 1:
                result.append(str(nums[0]))
                result.append(str(nums[1]))
            else:
                result.append(str(nums[0]) + "->" + str(nums[1]))
            return result
        
        start = nums[0]
        for i in range(1,len(nums)):
            if i == len(nums)-1:
                if nums[i]-nums[i-1] != 1:
                    result.append(str(start)+"->"+str(nums[i-1]))
                    result.append(str(nums[i]))
                else:
                    result.append(str(start)+"->"+str(nums[i]))
            elif nums[i]-nums[i-1] != 1:    
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(str(start)+"->"+str(nums[i-1]))
            start = nums[i]
        return result


# class Solution:
# 	def summaryRanges(self, nums: List[int]) -> List[str]:
# 		start = 0
# 		end = 0
# 		result = []

# 		while start < len(nums) and end<len(nums):
# 			if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
# 				end=end+1

# 			else:
# 				if start == end:
# 					result.append(str(nums[start]))
# 					start = start + 1
# 					end = end + 1
# 				else:
# 					result.append(str(nums[start])+'->'+str(nums[end]))
# 					start = end + 1
# 					end = end + 1

# 		return result
