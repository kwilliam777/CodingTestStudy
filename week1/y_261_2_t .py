class UnionFind :
    def __init__(self,n):
        self.parent = [node for node in range(n)]
        
    def Find(self, n) :
        if self.parent[n]==n :
            return n
        return self.Find(self.parent[n])
    
    def Union(self, a,b) :
        x=self.Find(a)
        y=self.Find(b)
        
        if x==y:
            return False
        
        self.parent[x]=y
        return True
    
    

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
       
       
        if n != len(edges)+1 :
            return False
        
        U=UnionFind(n)        
        
        for i,j in edges:
            if not U.Union(i,j):
                return False
            
        return True
