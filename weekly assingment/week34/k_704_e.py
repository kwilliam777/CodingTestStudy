class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minn,maxx = 0,len(nums) - 1
        ind = int()

        while minn <= maxx:
            ind = (minn + maxx) // 2
            if nums[ind] < target:
                minn = ind + 1
            elif nums[ind] > target:
                maxx = ind - 1
            else:
                return ind
        return -1
