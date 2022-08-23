class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictt = collections.defaultdict(list)
        for i in range(len(nums2)): 
            dictt[nums2[i]].append(i)
        nums1.sort()
        nums2.sort()
        res = [-1 for _ in range(len(nums1))]
        
        ind = 0
        for i in nums2:
            while ind < len(nums1) and nums1[ind] <= i: 
                ind+=1
            if ind == len(nums1): 
                break
            res[dictt[i].pop()] = nums1.pop(ind)
            
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = nums1.pop()
            
        return res
