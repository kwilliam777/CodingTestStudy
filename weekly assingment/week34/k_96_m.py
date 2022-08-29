class Solution:
    def numTrees(self, n: int) -> int:
        rec = [1]
        while len(rec) < n:
            step = rec[-1]*2
            if len(rec) >= 2:
                for i in range(len(rec)-1):
                    step += rec[i] * rec[len(rec)-2-i]
            rec.append(step)
        return rec[-1]
