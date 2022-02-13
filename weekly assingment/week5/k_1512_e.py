from collections import Counter
from itertools import combinations
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count, result = 0, Counter(nums)
        for i in result:
            if result[i] > 1: count += len(list(combinations([1]*result[i],2)))
        return count
