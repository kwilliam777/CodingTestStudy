from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ls = list(s)
        st = Counter(ls)
        uniq = [i for i in st if st[i]==1]
        ind = []
        for i in uniq:
            ind.append(ls.index(i))
        
        return min(ind) if len(ind) > 0 else -1
        
        
