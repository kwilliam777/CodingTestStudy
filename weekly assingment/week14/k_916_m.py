from collections import Counter 
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2 = Counter(words2[0])
        for i in range(1,len(words2)): w2+= Counter(words2[i])-w2

        ans = []
        for i in words1:
            temp = Counter(i)
            if len(w2 - temp) == 0: ans.append(i)

        return ans
    
    
#     def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
#         superset_b = reduce(lambda x, y: x | y, map(Counter, B))
#         return [a for a in A if superset_b & Counter(a) == superset_b]
    
    
# class Solution(object):
#     def wordSubsets(self, A, B):
#         def count(word):
#             ans = [0] * 26
#             for letter in word:
#                 ans[ord(letter) - ord('a')] += 1
#             return ans

#         bmax = [0] * 26
#         for b in B:
#             for i, c in enumerate(count(b)):
#                 bmax[i] = max(bmax[i], c)

#         ans = []
#         for a in A:
#             if all(x >= y for x, y in zip(count(a), bmax)):
#                 ans.append(a)
#         return ans
