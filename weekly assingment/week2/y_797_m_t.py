class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
       
        _visit=[0 for i in range(0,n)]
        _path=[]
        _answer=[]
        
        def DFS (start, end, graph, _visit,_path,_answer):
            _path.append(start)
            _visit[start]+=1
            
            if start==end :
                a_path=[]
                for i in _path :
                    a_path.append(i)
                _answer.append(a_path)
             
            else :
                for i in graph[start]:
                    if _visit[i] ==0 :
                        DFS(i,end, graph, _visit, _path, _answer)
                        del _path[-1] 
                        _visit[i]-=1
            
            return _answer
                            
        return DFS(0,n-1, graph, _visit,_path,_answer)