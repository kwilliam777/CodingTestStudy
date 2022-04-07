class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(dp)):
            if i == 0: dp[0] = nums[0]
            elif i == 1: dp[1] = nums[1]
            elif i == 2: dp[2] = nums[0]+nums[2]
            else:
                dp[i] = max(dp[i-2],dp[i-3])+nums[i]

        return max(dp)
