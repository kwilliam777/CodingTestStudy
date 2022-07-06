class Solution:
    def fib(self, n: int) -> int:
        res = [0,1]
        while len(res)<=n: res.append(res[-1]+res[-2])
        return res[n]
    
# class Solution:
#     def fib(self, N: int) -> int:
#     	a, b = 0, 1
#     	for i in range(N): a, b = b, a + b
#     	return a
