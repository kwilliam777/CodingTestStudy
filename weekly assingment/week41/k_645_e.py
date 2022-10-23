from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rec = Counter(nums)
        miss,dup = -1,-1
        for i in range(1,len(nums)+1):
            if i not in rec: miss = i
            elif rec[i] > 1: dup = i
        return [dup,miss]
