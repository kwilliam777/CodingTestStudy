class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans = {}
        for a,b in edges:
            if a not in ans: ans[a] = 1
            else: ans[a]+=1
            if b not in ans: ans[b] = 1
            else: ans[b]+=1
        l = len(edges)
        for i in ans:
            if ans[i]==l: return i
        
                
        # return edges[0][0] if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1] else edges[0][1]
        # x,y = edges[0][0], edges[0][1]
        # if x==edges[1][0] or x == edges[1][1]:
        #     return x
        # return y
