class Solution:
    def tribonacci(self, n: int) -> int:
        saver=[-1]*(38)
        saver[0]=0
        saver[1]=1
        saver[2]=1
        
        def _T(n) :
            if saver[n] != -1 :
                return saver[n]
            else :
                saver[n]= _T(n-3) + _T(n-2) + _T(n-1)
                return saver[n]
        
        return _T(n)
        
        
    
        