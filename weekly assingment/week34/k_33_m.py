class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minn,maxx = 0,len(nums) - 1
        while minn <= maxx:
            ind = (minn + maxx) // 2
            if target == nums[ind]: return ind
            elif nums[minn] <= nums[ind]:
                (maxx,minn) = (ind-1,minn) if nums[minn]<=target<=nums[ind] else (maxx,ind+1)
            elif nums[minn] > nums[ind]:
                (maxx,minn) = (maxx,ind+1) if nums[ind]<=target<=nums[maxx] else (ind-1,minn)
        return -1
