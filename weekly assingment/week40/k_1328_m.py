class Solution:
    def breakPalindrome(self, pal: str) -> str:
        if len(pal) == 1: return ""
        elif len(pal) == pal.count("a"): return pal[:-1]+"b"
        res = ""
        for i in range(len(pal)):
            if pal[i] != "a":
                temp = pal[:i]+"a"+pal[i+1:]
                if temp != temp[::-1]:
                    res = temp
                    break
            elif i == len(pal)-1: 
                res = pal[:-1]+"b"
        return res
