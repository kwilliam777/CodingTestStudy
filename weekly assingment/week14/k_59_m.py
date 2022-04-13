class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]
        ans = [[0 for i in range(n)] for i in range(n)]
        ind,val = 0,1
        way, cur = [[0,1],[1,0],[0,-1],[-1,0]],[0,0]
        
        while True:
            ans[cur[0]][cur[1]] = val
            val+=1
            nxt = [cur[0]+way[ind][0],cur[1]+way[ind][1]]
            if not (0<=nxt[0]<n and 0<=nxt[1]<n) or ans[nxt[0]][nxt[1]]!=0:
                ind+=1
                ind = ind%4
                nxt = [cur[0]+way[ind][0],cur[1]+way[ind][1]]
                if ans[nxt[0]][nxt[1]]!=0: break
            cur = nxt
        return ans
    
    
#     def generateMatrix(self, n):
#         A, lo = [], n*n+1
#         while lo > 1:
#             lo, hi = lo - len(A), lo
#             A = [range(lo, hi)] + zip(*A[::-1])
#         return A
