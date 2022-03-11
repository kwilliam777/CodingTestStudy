class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])
    
    
    
# import math
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         #raises 2 to the power a
#         fact1=math.pow(2,a)
#         #raises 2 to the power b
#         fact2=math.pow(2,b)
#         #by multiplying the 2 factors, the powers gets added
#         #ie, 2^(a+b)
#         prod=fact1*fact2
#         """
#          here we use the Log of Exponent Rule 
#             -> log2(2^(a+b)) = a+b
#          """
#         ans=math.log2(prod)
#         return int(ans)  
