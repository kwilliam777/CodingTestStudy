class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums.count(0) == len(nums): return "0"
        nums = sorted([str(i) for i in sorted(nums,reverse = True)],key = lambda x:len(x))
        nums = sorted(nums,key = lambda x:x[0],reverse = True)        
        for i in range(len(nums)-1):
            piv = 0
            while int(nums[i+piv]+nums[i+1+piv])<int(nums[i+1+piv]+nums[i+piv]):
                (nums[i+piv],nums[i+1+piv])=(nums[i+1+piv],nums[i+piv])
                piv -= 1
                if piv + i < 0:
                    break
        return ('').join(nums)
    
    
    
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         nums = list(map(str, nums))
#         cmp = lambda x, y: ((x+y) > (y+x)) - ((x+y) < (y+x))
#         nums = sorted(nums, key=cmp_to_key(cmp))
#         return str(int(''.join(nums[::-1])))
