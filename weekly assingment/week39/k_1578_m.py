class Solution:
    def minCost(self, colors: str, t: List[int]) -> int:
        tot = 0
        rec = [t[0]]
        for i in range(1,len(colors)):
            if colors[i-1]==colors[i]:
                rec.append(t[i])
            else:
                rec.sort()
                tot+=sum(rec[:-1])
                rec = [t[i]]
        if len(rec)>1:
            rec.sort()
            tot+=sum(rec[:-1])
        return tot
