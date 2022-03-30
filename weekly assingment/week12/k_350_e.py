class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
                nums2.remove(nums1[i])
        return ans 
    
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         a=collections.Counter(nums1)
#         b=collections.Counter(nums2)
#         #a={1:2,2:2}
#         #b={2:2}
#         #(a&b)<- this only returns the intersection value, not how many times that's why (a&b).elements()
#         return (a&b).elements()
