class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        track,index = {}, 0
        for i in range(len(nums)):
            if nums[index] in track:
                if track[nums[index]] >= 2: nums.remove(nums[index])
                elif track[nums[index]] < 2:
                    track[nums[index]] += 1
                    index += 1
            else:
                track[nums[index]] = 1
                index += 1
        return len(nums)