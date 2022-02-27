from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1 = Counter(s)
        t1 = Counter(t)
        count = 0
        for i in s1:
            if i not in t1:
                count += s1[i]
                t1[i] = s1[i]
            else:
                temp = s1[i]-t1[i] if s1[i] > t1[i] else 0
                s1[i] += temp
                count += temp
        
        for i in t1:
            if i not in s1:
                count += t1[i]
                s1[i] = t1[i]
            else:
                temp = t1[i] - s1[i] if t1[i] > s1[i] else 0
                t1[i] += temp
                count += temp
                
            
        return count
    
    
    
    
    
# class Solution:
#     def minSteps(self, s: str, t: str) -> int:
#         hmap_s = collections.Counter(s)
#         hmap_t = collections.Counter(t)
#         return sum((hmap_s-hmap_t).values()) + sum((hmap_t-hmap_s).values())
