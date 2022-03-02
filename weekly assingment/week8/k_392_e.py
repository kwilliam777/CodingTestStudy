class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        result = [0]
        for l in s:
            if l not in t: return False
            else:
                temp = t.index(l)
                result.append(temp+result[-1]+1)
                t=t[temp+1:]
                
        if len(s)!=len(result[1:]):
            return False
        elif result[1:] == sorted(result[1:]):
            return True
        else:
            return False
        
        
        
# class Solution(object):
#     def isSubsequence(self, s, t):
#         if not s: return True
#         i = 0
#         for char in t:
#             if char == s[i]:
#                 i += 1
#             if i == len(s): return True
#         if i != len(s): return False
