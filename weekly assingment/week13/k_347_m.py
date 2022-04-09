from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = dict(Counter(nums))
        ans = sorted([[i,nums[i]] for i in nums],key= lambda x:x[1],reverse = True)
        return [i[0] for i in ans][:k]
