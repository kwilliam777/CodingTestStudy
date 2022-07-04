class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)),reverse = True)
        if len(nums)<3:
            return nums[0]
        return nums[2]
    
    
    
    
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#     	n, T = list(set(nums)), [float('-inf')]*3
#     	for i in n:
#     		if i > T[0]:
#     			T = [i,T[0],T[1]]
#     			continue
#     		if i > T[1]:
#     			T = [T[0],i,T[1]]
#     			continue
#     		if i > T[2]:
#     			T = [T[0],T[1],i]
#     	return T[2] if T[2] != float('-inf') else T[0]
