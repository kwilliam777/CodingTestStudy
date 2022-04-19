class Solution:
    def generateTheString(self, n: int) -> str:
        blen = 0
        if n%2==0:
            alen = n-1
            blen = 1
        if blen==0:ans="a"*n
        else:ans="a"*alen+"b"
            
        return ans
    
        # return "a" * n if n % 2 else "a" * (n - 1) + "b"
