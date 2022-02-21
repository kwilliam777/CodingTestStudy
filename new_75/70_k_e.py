class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1,2,3]
        if n <= 3: return fib[n-1]
        for i in range(2, n): fib.append(fib[i-1]+fib[i])
        return fib[-2]
