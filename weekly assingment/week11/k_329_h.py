from operator import add

class Solution:
    def longestIncreasingPath(self, strArr: List[List[int]]) -> int:
        dp = [[-1 for j in range(len(strArr[0]))] for i in range(len(strArr))]
        up = [-1,0]
        down = [1,0]
        right = [0,1]
        left = [0,-1]
        dp[0][0]=10

        def isValid(loc):
            if 0 <= loc[0] < len(strArr) and 0 <= loc[1] < len(strArr[0]):
                return True
            else:
                return False

        def find(i,j):
            u = list(map(add,[i,j],up))
            d = list(map(add,[i,j],down))
            r = list(map(add,[i,j],right))
            l = list(map(add,[i,j],left))
            save = []
            stop = []

            if isValid(u):
                if strArr[u[0]][u[1]] < strArr[i][j]:
                    if dp[u[0]][u[1]] == -1:
                        find(u[0],u[1])
                    save.append(dp[u[0]][u[1]])
                    stop.append(False)
                else:
                    save.append(0)
                    stop.append(True)

            if isValid(d):
                if strArr[d[0]][d[1]] < strArr[i][j]:
                    if dp[d[0]][d[1]] == -1:
                        find(d[0],d[1])
                    save.append(dp[d[0]][d[1]])
                    stop.append(False)
                else:
                    save.append(0)
                    stop.append(True)

            if isValid(r):
                if strArr[r[0]][r[1]] < strArr[i][j]:
                    if dp[r[0]][r[1]] == -1:
                        find(r[0],r[1])
                    save.append(dp[r[0]][r[1]])
                    stop.append(False)
                else:
                    save.append(0)
                    stop.append(True)

            if isValid(l):
                if strArr[l[0]][l[1]] < strArr[i][j]:
                    if dp[l[0]][l[1]] == -1:
                        find(l[0],l[1])
                    save.append(dp[l[0]][l[1]])
                    stop.append(False)
                else:
                    save.append(0)
                    stop.append(True)

            if stop.count(True) == len(stop) and dp[i][j] == -1:
                dp[i][j] = 1
            else:
                save.append(0)
                dp[i][j] = max(save)+1

        for i in range(len(strArr)):
            for j in range(len(strArr[i])):
                find(i,j)

        ans = max([max(j) for j in dp])

        return ans

