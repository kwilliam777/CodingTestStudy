class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                good.append(num[i:i+3])
                
        return "" if len(good)==0 else max(good)