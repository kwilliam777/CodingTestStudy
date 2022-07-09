from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        save = Counter(arr)
        res = Counter(save.values())
        return True if len(save)==len(res) else False
