class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps={0:-1}
        cumSum=maxSoFar=0
        for i,num in enumerate(nums):
            if num==1:
                cumSum+=1
            else:
                cumSum-=1
            if cumSum in maps:
                maxSoFar=max(maxSoFar,i-maps[cumSum])
                
            else:
                maps[cumSum] = i
        
        return maxSoFar
                
        
        