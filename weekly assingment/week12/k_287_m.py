from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = Counter(nums)
        return [i for i in arr if arr[i] > 1][0]
