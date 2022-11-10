class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = s[0]
        for i in range(1,len(s)):
            if len(res)>0 and res[-1] == s[i]: res=res[:-1]
            else: res+=s[i]
        return res
