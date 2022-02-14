from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        check  = Counter(p)
        result = []
        for i in range(len(s)-len(p)+1):
            if s[i] in p:
                if i-1 in result and s[i-1] == s[i+len(p)-1]:
                    result.append(i)
                else:
                    temp = Counter(s[i:i+len(p)])
                    if temp == check:
                        result.append(i)
        return result 

#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         hm, res, pL, pS = defaultdict(int), [], len(p), len(s)
#         if pL > pS: return []

#         # build hashmap
#         for ch in p: hm[ch] += 1

#         # initial full pass over the window
#         for i in range(pL-1):
#             if s[i] in hm: hm[s[i]] -= 1

#         # slide the window with stride 1
#         for i in range(-1, pS-pL+1):
#             if i > -1 and s[i] in hm:
#                 hm[s[i]] += 1
#             if i+pL < pS and s[i+pL] in hm: 
#                 hm[s[i+pL]] -= 1

#             # check whether we encountered an anagram
#             if all(v == 0 for v in hm.values()): 
#                 res.append(i+1)

#         return res
        
