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
