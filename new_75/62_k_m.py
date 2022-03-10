import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))
        return comb(n+m-2, m-1)
    
    
    
    
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         results = []
#         for i in range(m):
#             results.append([0]*n)
#             for j in range(n):
#                 if i==0 or j==0:
#                     results[i][j] = 1
#                 else:
#                     results[i][j] = results[i-1][j]+results[i][j-1]
#         return results[-1][-1]
