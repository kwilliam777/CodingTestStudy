class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1
        elif n == 2: return 1 if isBadVersion(1) else 2
        
        ind = n
        init = isBadVersion(ind)
        comp = isBadVersion(ind-1)
        high = n
        low = 0
        
        while init==comp:
            if init == True: high = ind
            else: low = ind+1

            ind = (high+low)//2+1 if high-low > 2 else high-1
            init = isBadVersion(ind)
            comp = isBadVersion(ind-1)  
            
        return ind
