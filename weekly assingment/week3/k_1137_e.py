class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0,1,1]
        if n <= 2: return tri[n]
        
        for i in range(n-2):
            tri.append(tri[i]+tri[i+1]+tri[i+2])
            
        return tri[n]