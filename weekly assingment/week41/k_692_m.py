from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        rec = sorted(Counter(words).items(), key=lambda x:x[0])
        rec = sorted(rec,key=lambda x:x[1],reverse = True)
        return [i[0] for i in rec][:k]
