class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        temp = list("".join(s.split("-")))
        for i in range(len(temp)):
            if temp[i].islower(): temp[i] = temp[i].upper()
        temp = "".join(temp)
        first = len(temp)%k
        result = str(temp[:first])
        temp = temp[first:]
        for i in range(len(temp)//k):
            if len(result) == 0: result += temp[i*k:(i+1)*k]    
            else: result += "-" + temp[i*k:(i+1)*k]
        return result
# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         s=s.replace("-","").upper()
#         s=s[::-1]
#         ans=[]
#         for i in range(0,len(s),k):
#             (ans.append(s[i:i+k]))
#             ans.append('-')
#         if(len(ans)!=0):
#             ans.pop()
#         ans=("".join(str(e) for e in  ans))
#         ans=ans[::-1]
#         return (ans)