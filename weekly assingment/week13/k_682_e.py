class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for i in ops:
            if i.isnumeric() or i[0] == "-": scores.append(int(i))
            elif i == "D": scores.append(scores[-1]*2)
            elif i == "C": scores.pop()
            elif i == "+": scores.append(sum(scores[-2:]))
        return sum(scores)
