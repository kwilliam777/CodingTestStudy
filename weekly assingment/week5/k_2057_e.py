class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        result = [i for i in range(len(nums)) if i%10 == nums[i]]
        return min(result) if len(result) > 0 else -1
