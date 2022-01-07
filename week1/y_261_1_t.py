class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
                
        if n ==1 :
            return True
        
        if n <1:
            return False
        
        if len(edges)==0 :
            return False
        
        _stack=[]
        _vistited=[0]*n
        _stack.append(edges[0][0])
        
        count=0
        while len(_stack) > 0 :
            count+=1
            a=_stack.pop()
            _vistited[a]+=1
            
            if _vistited[a]>1 :
                return False
            
            for e in edges :
                if e[0]== a :
                    _stack.append(e[1])
                    e[0]="v"
                    e[1]="v"
                elif e[1]== a:
                    _stack.append(e[0])
                    e[0]="v"
                    e[1]="v"

                    
        for i in _vistited :
            if i ==0 :
                return False
                    
        return True
                    
  
        