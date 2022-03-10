class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        elif len(nums) == 2 and nums[0] >= 1: return True
        elif nums[0] == 0: return False
        nums = nums[::-1]
        ind = [i for i in range(len(nums)) if nums[i] >= i and i > 0]
        count = 0
        if len(ind) == 0: return False
        while len(nums)-1 not in ind:
            temp = len(ind)
            [[ind.append(i+j) for i in range(len(nums[j:])) if nums[i]>=i and i+j not in ind] for j in ind]
            print(ind)
            if temp == len(ind):
                count += 1
            if count > 1000:
                return False
        return True

    
#     def canJump(self, nums: List[int]) -> bool:
#         position = len(nums) - 1
        
#         for i in range(len(nums) - 2, -1, -1):
#             if nums[i] + i >= position:
#                 position = i
#         return position == 0
