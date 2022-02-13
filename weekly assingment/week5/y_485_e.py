class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answ=[]
        
        answ.append(0)
        
        for index, data in enumerate(nums):
            if data ==1:
                answ.append(answ[index]+1)
            else :
                answ.append(0)
                
        return max(answ)
