from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        data = sorted(Counter(s).values(),reverse = True)
        count = 0
        for i in range(len(data)):
            temp = data.pop(0)
            while temp > 0 and temp in data:
                count += 1
                temp -= 1
            data.append(temp)
        return count
