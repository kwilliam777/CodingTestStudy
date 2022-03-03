class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        temp = [nums[i]- nums[i-1] for i in range(1,len(nums))]

        counts = []
        count = 1
        pre = temp[0]
        for i in range(1,len(temp)):
            if i == len(temp)-1:
                if pre == temp[i]:
                    count += 1
                    counts.append(count)
                else:
                    counts.append(count)
                    counts.append(1)
            if pre == temp[i]:
                count += 1
                pre = temp[i]
            else:
                counts.append(count)
                pre = temp[i]
                count = 1
        counts = [i for i in counts if i >= 2]
        
        result = 0
        for i in counts:
            t = i-1
            for j in range(t):
                result += j+1
        return result

    
    
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         cur_diff, cnt = -1, 0
#         res = 0
#         for i in range(1, len(nums)):
#             new_diff = nums[i] - nums[i-1]
#             if new_diff != cur_diff:
#                 cur_diff, cnt = new_diff, 1
#             else:
#                 res += cnt
#                 cnt += 1
#         return res
