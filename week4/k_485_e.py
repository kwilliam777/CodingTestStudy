class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.insert(0,0)
        nums.append(0)
        term = [i for i in range(len(nums)) if nums[i] == 0]
        result = [term[i] - term[i-1] for i in range(1, len(term))]
        return max(result) - 1