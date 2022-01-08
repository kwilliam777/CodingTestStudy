class Solution:    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def dfs(visited, adj_edge, node) :  
            visited[node] = 1           
            for i in adj_edge[node] :               
                if visited[i] == 0 :
                    dfs (visited, adj_edge, i)
        
        adj_edge=[]
        for i in range(0, n) :
            adj_edge.append([])
            
        logs.sort()
        print(logs)
            
        for data in logs :
            adj_edge[data[1]].append(data[2])
            adj_edge[data[2]].append(data[1])
            vistied =[0]*n
            dfs(vistied,adj_edge,data[1])
            checker = 1
            for i in vistied :
                checker *=i
            if checker != 0 :
                return data[0]        
        return -1
            
    
        
      
    
        