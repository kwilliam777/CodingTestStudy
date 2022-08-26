class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def conv(s):
            res = []
            for i in s:
                if i!="#": res.append(i)
                elif len(res)>0: res.pop()
            return "".join(res)
        return conv(s)==conv(t)  
