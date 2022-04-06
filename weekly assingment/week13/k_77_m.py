from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations([i for i in range(1,n+1)],k)
        
        
        
# class Solution:
#     def combine(self, n, k):
#         if k == 0:
#             return [[]]
#         return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

    
# class Solution:
#     def combine(self, n, k):
#         combs = [[]]
#         for _ in range(k):
#             combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
#         return combs
    
    
# class Solution:
#     def combine(self, n, k):
#         return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)], range(k), [[]])
