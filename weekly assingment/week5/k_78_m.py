class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        if len(nums) == 1: 
            result.append([nums[0]])
            return result
        for i in nums: result.append([i])
        
        done, ind = False, -1
        
        while not done:
            ind += 1
            for num in nums:
                if num not in result[ind]:
                    temp = copy.deepcopy(result[ind])
                    temp.append(num)
                    if temp != None: temp = sorted(temp)
                    if temp not in result: result.append(temp)
            if nums in result: done = True
                
        return result
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = [[]]
        
#         for num in nums:
#             output += [curr + [num] for curr in output]
        
#         return output
