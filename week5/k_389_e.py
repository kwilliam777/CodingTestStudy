class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1: return t
        temp = list(t)
        for l in s: 
            if l in temp: temp.remove(l)
        return "".join(temp)
