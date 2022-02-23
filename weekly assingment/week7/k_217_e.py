from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        if max(nums.values()) > 1:
            return True
        return False
        # return len(nums) != len(set(nums))
