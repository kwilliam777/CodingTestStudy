class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        track,index = set(), 0
        for i in range(len(nums)):
            temp = nums.pop(index)
            index -= 1
            if temp+k in nums: track.add((temp, temp+k))
            index += 1
            nums.insert(index,temp)
            index += 1
        return len(track)
        

        