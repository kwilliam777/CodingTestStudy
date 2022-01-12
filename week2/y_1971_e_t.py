class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_Edges=[]
        
        for i in range(n):
            adj_Edges.append([])
            
        for _from, _to in edges:
            adj_Edges[_from].append(_to)
            adj_Edges[_to].append(_from)
            
        _visit=[0 for i in range(0,n)]
        
        answer=0
        print(adj_Edges)
        
        
        def dfs(start,end,_visit,adj_Edges,answer) :
            _visit[start]+=1
            if start == end :
                answer+=1
                return answer
            else :
                for _n in adj_Edges[start] :
                    if _visit[_n] ==0 :
                        answer += dfs(_n,end,_visit,adj_Edges,answer)
                        
            return answer
        

        if dfs(start,end,_visit,adj_Edges,answer) :
            return True
        else :
            return False