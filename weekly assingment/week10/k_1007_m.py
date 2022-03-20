from collections import Counter
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        temp = Counter(tops + bottoms)
        val = max(temp, key = temp.get)
        count = 0
        same = 0
        if temp[val] < len(tops): return -1
        for i in range(len(tops)):
            if tops[i]!=val and bottoms[i]!=val:
                return -1
            elif tops[i] == val:
                if tops[i] == bottoms[i]:
                    same += 1
                else:
                    count += 1
                
        return min(count, len(tops)-same-count)
