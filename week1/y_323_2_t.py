class UnionFind :
    def __init__ (self,n):
        self.parent = [node for node in range(0,n)]
        
    def Find(self, n) :
        if self.parent[n]==n :
            return n
        
        return self.Find(self.parent[n])
        
    def Union (self, a,b) :
        x=self.Find(a)
        y=self.Find(b)
        if x==y :
            return False
        
        self.parent[x]=y
        return True
            

class Solution:    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if not edges :
            return n
        
        U=UnionFind(n)
        
        for i in edges:
            U.Union(i[0],i[1])
            
        _visited=[]
        _visited.append(edges[0][0])
        count =1
            
        for i in range(0,n):
            for j in _visited :
                if U.Union(i,j) :
                    _visited.append(i)
                    count +=1
                
        return count
            
      