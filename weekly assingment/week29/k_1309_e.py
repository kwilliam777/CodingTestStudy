class Solution:
    def freqAlphabets(self, s: str) -> str:
        # ind = len(s)-1
        # res = str()
        # while ind >= 0:
        #     if s[ind] == "#":
        #         res = chr(int(s[ind-2:ind])+96)+res
        #         ind -= 3
        #     else:
        #         res = chr(int(s[ind])+96)+res
        #         ind -= 1
        # return res
                
        
        
        vals = []
        for i in s:
            if i == "#":
                pre1 = vals.pop()
                pre2 = vals.pop()
                vals.append(pre2+pre1)
            else:
                vals.append(i)
        
        return "".join([chr(int(i)+96) for i in vals])
