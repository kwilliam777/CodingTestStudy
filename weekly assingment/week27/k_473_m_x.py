class Solution:
    def makesquare(self, M: List[int]) -> bool:
        n, side = len(M), sum(M) / 4
        M.sort(reverse=True)
        if side != int(side) or M[0] > side:
            return False
        def btrack(i, space, done): 
            if done == 3:
                return True
            while i < n:
                num = M[i]
                if num > space:
                    i += 1
                    continue
                M[i] = side + 1
                if num == space:
                    res = btrack(1, side, done+1)
                else:
                    res = btrack(i+1, space-num, done)
                if res:
                    return True
                M[i] = num
                while i < n and M[i] == num:
                    i += 1
            return False
        return btrack(0, side, 0)
    
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        value = sum(matchsticks)
        if value < 4:
            return False
        if value % 4 != 0:
            return False
        edge = value // 4
        matchsticks.sort(reverse=True)
        @cache
        def findedges(l1, l2, l3, l4, i):
            nonlocal edge
            if l1 == l2 == l3 == l4 == edge:
                return True
            if i > len(matchsticks) - 1:
                return False
            if l1 > edge or l2 > edge or l3 > edge or l4 > edge:
                return False
            return findedges(l1 + matchsticks[i], l2, l3, l4, i + 1) or findedges(l1, l2 + matchsticks[i] , l3, l4, i + 1) or findedges(l1, l2, l3 + matchsticks[i], l4, i + 1) or findedges(l1, l2, l3, l4 + matchsticks[i] , i + 1)
        return findedges(0, 0, 0, 0, 0)
