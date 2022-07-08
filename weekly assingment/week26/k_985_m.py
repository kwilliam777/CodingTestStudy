class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        odd = []
        tot = 0
        
        for i in nums:
            if i%2==0:
                odd.append(0)
            else:
                odd.append(i)
        tot = sum(nums)-sum(odd)
        
        for val,ind in queries:
            if odd[ind]!=0:
                if val%2==0:
                    nums[ind]+=val
                else:
                    nums[ind]+=val
                    tot+=nums[ind]
                    odd[ind]=0
            else:
                if val%2==0:
                    nums[ind]+=val
                    tot+=val
                else:
                    tot-=nums[ind]
                    nums[ind]+=val
                    odd[ind]=nums[ind]
            res.append(tot)
        return res
                    
    
# class Solution:
#     def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
#         sum_even = sum(filter(lambda n: n % 2 == 0, A))
        
#         result = []
#         for val, idx in queries:
#             if A[idx] % 2 == 0:
#                 if val % 2 == 0:
#                     sum_even += val
#                 else:
#                     sum_even -= A[idx]
#             elif val % 2 == 1:
#                     sum_even += A[idx] + val

#             A[idx] += val
#             result.append(sum_even)
                
#         return result
