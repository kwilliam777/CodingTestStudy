class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n==1 or n==2: return ["1/2"]
        ans = []
        for i in range(2,n+1):
            for j in range(1,i):
                for k in range(1,i):
                    if not (i%k==0 and j%k==0):
                        ans.append(str(j)+"/"+str(i))
                        break
                    
        return sorted(ans)
    
#XXXXXXXXXXXXXXXX
#     def simplifiedFractions(self, n: int) -> List[str]:
#         s = set() 
#         ans = []
#         for i in range(2,n+1): # we search the denominator from small to large
#             for j in range(1,i): # if a fraction is not simplified, its simplified version must be searched before 
#                 if j/i not in s:
#                     s.add(j/i)
#                     ans.append(str(j) + "/" + str(i))
#         return ans
