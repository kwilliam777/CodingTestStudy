class UnionFind:
    def __init__(self, _temp):
        self.root = {}
        self.rank = {}
        
        for i in _temp:
            self.root[i] = i
            self.rank[i] = 1

    def Find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.Find(self.root[x])
        return self.root[x]

    def Union(self, a, b):
        a_r = self.Find(a)
        b_r = self.Find(b)

        if a_r == b_r:
            return False

        if self.rank[a_r] > self.rank[b_r]:
            self.root[b_r] = a_r

        elif self.rank[a_r] < self.rank[b_r]:
            self.root[a_r] = b_r

        else:
            self.root[b_r] = a_r
            self.rank[a_r] += 1

    def Check(self, a, b):
        a_r = self.Find(a)
        b_r = self.Find(b)

        if a_r == b_r:
            return True
        else:
            return False



class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        _temp=set()        
        for i in equations :
            _temp.add(i[0])
            _temp.add(i[1])
            
            
        adj_edge = defaultdict(defaultdict) 
        edge_list ={}
        U=UnionFind(_temp)
        
        for edge in equations :               
            U.Union(edge[0],edge[1])             
        
        for i,data in enumerate(equations) :
            adj_edge[data[1]][data[0]] =  (1/values[i])
            adj_edge[data[0]][data[1]] = values[i]
            if data[0] not in edge_list:
                edge_list[data[0]] =[data[1]]
            else :
                edge_list[data[0]].append(data[1])
                
            if data[1] not in edge_list:
                edge_list[data[1]] =[data[0]]
            else :
                edge_list[data[1]].append(data[0])
                                    

        def DFS (_from, _to , value ,_visit) :
            _visit.append(_from)
            answer=-1
            
            if _to in edge_list[_from]:
                answer= value * adj_edge[_from][_to]
            else:
                for neighbour in edge_list[_from] :
                    if neighbour not in _visit :
                        value = value * adj_edge[_from][neighbour]
                        answer = DFS (neighbour, _to , value, _visit)
                        value = value / adj_edge[_from][neighbour]
                    if answer != -1.0 :
                        break   
            _visit.remove(_from)    
            return answer

            
        _k=[]    
        
        _answer=[]
        for i in queries :
            
            if i[0] not in _temp or i[1] not in _temp :
                _answer.append(-1.0)
                
            elif i[0]==i[1] :
                _answer.append(1.0)
            
            elif not U.Check(i[0],i[1]) :
                _answer.append(-1.0)
                
            else :
                _visit=[]
                _answer.append(DFS(i[0],i[1],1.0,_visit=[]))
                 
        return _answer
     