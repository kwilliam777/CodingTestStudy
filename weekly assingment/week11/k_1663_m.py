class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = [1]*n
        k -= n
        ind = n-1
        
        while k != 0:
            temp = 25 if k>=25 else k
            result[ind]+=temp
            ind-=1
            k -= temp
        
        return ("").join([chr(i+96) for i in result])
        
# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         z, alp = divmod(k-n-1, 25)
#         return (n-z-1)*'a'+chr(ord('a')+alp+1)+z*'z'
