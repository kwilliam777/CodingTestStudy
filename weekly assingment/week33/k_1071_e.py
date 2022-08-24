class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        (long,short) = (str2,str1) if len(str1)<=len(str2) else (str1,str2)
        arr = [i for i in range(1,len(short)+1) if len(short)%i==0][::-1]
        
        for i in arr:
            if short[:i]*(len(short)//i)==short and short[:i]*(len(long)//i)==long:
                return short[:i]
        return ""
