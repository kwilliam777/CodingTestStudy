class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        check = []
        suspect = {}
        if n == 1:
            return 1
        elif n == 2 and len(trust) ==1:
            return trust[0][1]
        for i in trust:
            check.append(i[0])
            if i[1] in suspect:
                suspect[i[1]].append(i[0])
            else:
                suspect[i[1]] = [i[0]]

        for i in suspect:
            if i not in check and len(suspect[i]) == n-1:    
                return i
        return -1