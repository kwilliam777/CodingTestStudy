class UnionFind :
    def __init__ (self, n) :
        self.root =[i for i in range(n)]
        self.rank =[1]*n
        
    def find(self, x) :
        if self.root[x]==x :
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    
    def union(self, a, b) :
        x=self.find(a)
        y=self.find(b)
        
        if x==y :
            return False
        
        if self.rank[x] > self.rank[y] :
            self.root[y]=x
        elif self.rank[x] < self.rank[y] :
            self.root[x]=y
        else :
            self.root[y]=x
            self.rank[x]+=1
            
        

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        U=UnionFind(n)
        
        
        for i in pairs:
            U.union(i[0],i[1])
            
        set_dict={}
        
        for i in range(0,n) :
            U.find(i)
        
        print(U.root)
        
        for index,data in enumerate(U.root) :
            if data not in set_dict :
                set_dict[data]=[index]
            else :
                set_dict[data].append(index)
           
        _answer=[0]*n
        
        print(set_dict)
        
        
        for key in set_dict :
            sub_st=[]
            print(set_dict[key])
            for data in set_dict[key]:
                sub_st.append(s[data])
            sub_st.sort()
            
            for index, data in enumerate (set_dict[key]):
                _answer[data] = sub_st[index]

        answer=""
        for i in _answer :
            answer+=i
            
        return answer
            
            
            
        