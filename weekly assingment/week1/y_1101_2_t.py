class UnionFind :
    def __init__ (self,n):
        self.parent = [node for node in range(0, n)]
        self.size=[1 for node in range(0,n)]
    
    def Find(self,n):
        if self.parent[n]==n:
            return n
        
        return self.Find(self.parent[n])
    
    def Union(self, a, b) :
        x=self.Find(a)
        y=self.Find(b)
        
        if x==y :
            return False
        
        elif self.size[x] >= self.size[y] :
            self.parent[y]=x
            self.size[x]+=self.size[y]
            
        else :
            self.parent[x]=y
            self.size[y]+=self.size[x]
            
    def Check_union(self, a, b) :
        x=self.Find(a)
        y=self.Find(b)
        
        if x==y :
            return True
        return False 


class Solution:    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
            
        U=UnionFind(n)
        logs.sort()
            
        for data in logs :
            U.Union(data[1],data[2])
            count=0
            for i in range(0,n) :
                if not U.Check_union(data[1],i) :
                    break
                count+=1
                if count == n :
                    return data[0]        
        return -1
            
    
        
      
    
        