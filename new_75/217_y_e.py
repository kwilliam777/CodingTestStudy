class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker={}
        
        for data in nums:
            if data in checker.keys() :
                return True
            else :
                checker[data]=1
        
        return False
                
