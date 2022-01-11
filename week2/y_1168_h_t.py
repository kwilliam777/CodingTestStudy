class UnionFind :
    def __init__(self,n) :
        self.root=[node for node in range(0,n+1)]
        self.rank=[1 for node in range(0,n+1)]
        
    def Find(self, x):
        if self.root[x]==x :
            return x
        
        self.root[x]=self.Find(self.root[x])
        return self.root[x]
        
    def Union(self,x,y):
        x_root=self.Find(x)
        y_root=self.Find(y)
        
        if x_root == y_root :
            return False
        
        if self.rank[x_root] > self.rank[y_root] :
            self.root[y_root]=x_root
            
        elif self.rank[x_root] < self.rank[y_root] :
            self.root[x_root]=y_root
            
        else :
            self.root[y_root]=x_root
            self.rank[x_root]+=1
        
        return True
            
    def Check(self, x,y):
        x_root=self.Find(x)
        y_root=self.Find(y)
        
        if x_root == y_root :
            return True
        else:
            return False
        
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        
        #Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
            
        
        for index,cost in enumerate(wells) :
            pipes.append([0,index+1,cost])
        
        pipes.sort(key=lambda row: (row[2]))
        
        
        U=UnionFind(n)
        
        answer=0
        
        for _from, _to, cost in pipes:
            if U.Union(_from, _to) :
                answer+=cost
        
        return answer
   
        
            
            