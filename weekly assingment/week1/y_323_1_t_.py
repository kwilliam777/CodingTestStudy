class Solution:    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        def dfs(adj_edge, _visited, _node) :
            _visited[_node]=1
            for adj_node in adj_edge[_node] :
                if _visited[adj_node]==0 :
                    dfs(adj_edge, _visited, adj_node)
        
        adj_edge=[]
              
        for i in range (n) :
            adj_edge.append([])
        
        for i in edges :
            adj_edge[i[0]].append(i[1])
            adj_edge[i[1]].append(i[0])

        _visited = [0]*n
        count=0
        
        for i in range(n) :
            if _visited[i] ==0 :
                dfs(adj_edge,_visited,i)
                count+=1
                
        return count